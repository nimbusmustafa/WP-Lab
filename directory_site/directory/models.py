# directory/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    number_of_visits = models.PositiveIntegerField(default=0)
    number_of_likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="pages")
    title = models.CharField(max_length=255)
    url = models.URLField()
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
