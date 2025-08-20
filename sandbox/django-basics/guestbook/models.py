from django.db import models

# Create your models here.
class Guest(models.Model):
    name = models.CharField("ФИО", max_length=100)
    message = models.TextField("Сообщение", max_length=1500)
    created_at = models.DateTimeField("Созданое говно", auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} -  <{self.message}>"
