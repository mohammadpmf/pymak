from django.db import models
# from django.contrib.auth.

class Post(models.Model):
    CHOICES = (
        ('pub', 'published'),
        ('drf', 'draft'),
    )
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3, choices=CHOICES)
    # author = models.ForeignKey()
    
    def __str__(self):
        return f"{self.title}"