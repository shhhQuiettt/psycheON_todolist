from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=128)
    done = models.BooleanField(default=False)
    author_ip = models.CharField(max_length=40)
    created_date = models.DateField(auto_now_add=True)
    done_date = models.DateField(blank=True, null=True)
