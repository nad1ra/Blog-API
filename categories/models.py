from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    desc = models.TextField()

