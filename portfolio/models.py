from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Portfolio_Project(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title