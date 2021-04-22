from django.db import models

# Create your models here.
class Todo(models.Model):
    descripcion = models.CharField(max_length=100, default="NA")
    done = models.BooleanField(default=False)