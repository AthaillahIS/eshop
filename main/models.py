from django.db import models


class Entry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()
    date = models.CharField(max_length=255)

    def __str__(self):
        return self.nameco