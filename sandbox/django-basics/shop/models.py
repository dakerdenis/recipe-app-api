from django.db import models

class Product(models.Model):
    title = models.CharField("Название", max_length=100)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    description = models.TextField("Описание", max_length=2000, blank=True)
    image = models.ImageField(
        "Фото",
        upload_to="products/%Y/%m/%d/",  # файлы попадут в media/products/ГОД/МЕСЯЦ/ДЕНЬ/
        blank=True,                       # можно оставить пустым на первых порах
    )
    created_at = models.DateTimeField("Создано", auto_now_add=True)

    def __str__(self):
        return self.title
