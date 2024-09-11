from django.db import models


class Entry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()
    date = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255, null=True)
    author_clas = models.CharField(max_length=255, null=True)
    app_name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nameco