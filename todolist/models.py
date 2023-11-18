from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=125)
    author = models.CharField(max_length=125)
    publication_date = models.DateField(auto_now_add=True)
