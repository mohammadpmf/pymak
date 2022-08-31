from django.db import models

class Note(models.Model):
    text = models.CharField(max_length=200)

class Note2(models.Model):
    title = models.CharField(max_length=50)
    detailed_text = models.CharField(max_length=200)
    full_description = models.TextField()
    author = models.CharField(max_length=50)
    age_author = models.DecimalField(max_digits=3, decimal_places=1)
    date_written = models.DateTimeField()

