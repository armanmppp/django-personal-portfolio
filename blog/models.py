from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    date = models.DateField()

    def __str__(self):
        return self.title