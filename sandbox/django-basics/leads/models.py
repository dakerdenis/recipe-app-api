from django.db import models

class Lead(models.Model):
    full_name = models.CharField("ФИО", max_length=100)
    email = models.EmailField("Email")
    message = models.TextField("Сообщение", max_length=2000)
    created_at = models.DateTimeField("Создано", auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} <{self.email}>"
