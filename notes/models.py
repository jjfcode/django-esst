from turtle import title
from venv import create
from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
