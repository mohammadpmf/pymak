from django.db import models

class Post(models.Model):
    CHOICES = (
        ('pub', 'published'),
        ('drf', 'draft'),
    )
    title = models.CharField(max_length=50)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=3, choices=CHOICES)
    author = models.ForeignKey(to='auth.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title}"