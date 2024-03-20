
from django.db import models

class FormData(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    links = models.URLField()
    documents = models.FileField(upload_to='documents/')
