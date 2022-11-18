from django.db import models

# Create your models here.
class Letter(models.Model):
    image = models.ImageField()

    def __str__(self):
        return self.title