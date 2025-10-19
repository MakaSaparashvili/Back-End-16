from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
