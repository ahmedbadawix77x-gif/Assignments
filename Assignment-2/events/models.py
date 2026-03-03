import uuid
from django.db import models


class Event(models.Model):
    # Chapter 1: Building the Foundation (Database)
    
    # A unique magical ID for every event
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # The title of the event
    name = models.CharField(max_length=255)
    
    # The story behind the event
    description = models.TextField()
    
    # Where the adventure happens
    location = models.CharField(max_length=255)
    
    # When the adventure begins
    start_date = models.DateTimeField()
    
    # When the adventure ends
    end_date = models.DateTimeField()
    
    # When the event was recorded
    created_at = models.DateTimeField(auto_now_add=True)
    
    # When the event details were last updated
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name