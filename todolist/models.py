from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=125, blank=False)
    Description = models.CharField(max_length=125, blank=True)
    post_date = models.DateField(blank=False)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
