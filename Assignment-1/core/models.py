from django.db import models

class Event(models.model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank= True, null=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    