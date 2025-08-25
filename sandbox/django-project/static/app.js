// helper для CSRF (если будем делать POST/PUT/DELETE с того же домена)
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}

const API = "/api/posts/"; // DRF router

async function fetchPosts() {
  const res = await fetch(API, { credentials: "same-origin" });
  const data = await res.json();
  const list = document.getElementById("posts");
  list.innerHTML = "";
  data.forEach((p) => {
    const li = document.createElement("li");
    li.innerHTML = `
      <strong>${p.title}</strong><br/>
      <small>${new Date(p.created_at).toLocaleString()}</small><br/>
      <span>${p.body}</span><br/>
      <button data-id="${p.id}" class="delete-btn">Удалить</button>
    `;
    list.appendChild(li);
  });
}
function renderErrors(errors) {
  const box = document.getElementById("errors");
  if (!errors || Object.keys(errors).length === 0) {
    box.textContent = "";
    return;
  }
  // errors выглядит как { title: ["..."], body: ["..."] }
  const list = Object.entries(errors)
    .map(([field, msgs]) => `${field}: ${msgs.join(", ")}`)
    .join(" | ");
  box.textContent = list;
}


async function createPost(title, body) {
  const res = await fetch("/api/posts/", {
    method: "POST",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken") || "",
    },
    body: JSON.stringify({ title, body }),
  });

  if (res.ok) {
    // 201 Created
    const json = await res.json();
    return { ok: true, data: json };
  }

  // если 400 — достаём JSON с ошибками и отдаём наверх
  let errors = {};
  try {
    errors = await res.json();
  } catch (_) {
    // на всякий случай
    errors = { non_field_errors: ["Что-то пошло не так"] };
  }
  return { ok: false, errors };
}

async function deletePost(id) {
  const res = await fetch(`${API}${id}/`, {
    method: "DELETE",
    credentials: "same-origin",
    headers: { "X-CSRFToken": getCookie("csrftoken") || "" },
  });
  if (!res.ok && res.status !== 204) {
    const err = await res.text();
    throw new Error(err);
  }
}

document.getElementById("create-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  renderErrors(null);

  const title = document.getElementById("title").value.trim();
  const body = document.getElementById("body").value.trim();

  const result = await createPost(title, body);

  if (!result.ok) {
    renderErrors(result.errors);
    return;
  }

  e.target.reset();
  await fetchPosts();
  renderErrors(null);
});

document.getElementById("posts").addEventListener("click", async (e) => {
  if (e.target.classList.contains("delete-btn")) {
    const id = e.target.getAttribute("data-id");
    await deletePost(id);
    fetchPosts();
  }
});

// инициализация
fetchPosts();
