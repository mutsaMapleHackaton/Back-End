from django.db import models

# Create your models here.
class Letter(models.Model):
    title = models.TextField(max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to='')

    def __str__(self):
        return self.title