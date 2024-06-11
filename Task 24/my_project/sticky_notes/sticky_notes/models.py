from django.db import models

# Create your models here.
class Note(models.Model):
     title = models.CharField(max_length=255)
     content = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
# Define a ForeignKey for the author's relationship
     author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True, blank=True)

class Author(models.Model):
     name = models.CharField(max_length=255)

