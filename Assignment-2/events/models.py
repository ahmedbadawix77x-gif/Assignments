import uuid
from django.db import models


class Event(models.Model):
    # Chapter 1: Building the Foundation (Database)
    # [MERGE NOTE]: This model replaces the one from Assignment-1/core/models.py
    # Change: 'id' was an AutoField in Assignment-1, now it's a UUIDField for better global uniqueness.
    # Change: 'title' was renamed to 'name' for consistency with other parts of the project.
    # Change: 'date' was split into 'start_date' and 'end_date' to support multi-day events.
    # Change: Added 'created_at' and 'updated_at' for better tracking.
    
    # A unique magical ID for every event
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # The title of the event (formerly 'title' in assignment-1)
    name = models.CharField(max_length=255)
    
    # The story behind the event
    description = models.TextField()
    
    # Where the adventure happens
    location = models.CharField(max_length=255)
    
    # When the adventure begins (formerly 'date' in assignment-1)
    start_date = models.DateTimeField()
    
    # When the adventure ends (new field from assignment-2)
    end_date = models.DateTimeField()
    
    # When the event was recorded
    created_at = models.DateTimeField(auto_now_add=True)
    
    # When the event details were last updated
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
