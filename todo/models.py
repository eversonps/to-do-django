from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=120)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)