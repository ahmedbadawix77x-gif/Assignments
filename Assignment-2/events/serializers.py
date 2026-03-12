from rest_framework import serializers
from .models import Event

# --- Educational Section: Comparison for Your Review ---

# WHAT WAS CHANGED/MISSING:
# In standard Django (Assignment-1 level), you might have used manual JSON responses or 
# basic Serializer classes. A basic 'serializers.Serializer' requires you to:
# 1. Explicitly define EVERY field (e.g., name = serializers.CharField()).
# 2. Manually implement create() and update() methods to save to the database.
# 3. Handle validation logic manually for each field.

"""
# EXAMPLE OF OUTDATED/LESS EFFICIENT APPROACH (Commented out):
class EventSerializerBasic(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    location = serializers.CharField(max_length=255)
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        # ... and so on for every field ...
        instance.save()
        return instance
"""

# --- NEW BEST PRACTICE IMPLEMENTATION ---

# DRF BEST PRACTICE: Use ModelSerializer.
# Why? 
# 1. AUTOMATION: It automatically generates fields based on your Model (Event).
# 2. EFFICIENCY: It provides default implementations for create() and update().
# 3. CONSISTENCY: It automatically handles validation defined in your models (like max_length).

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        # ID and timestamps should be read-only as they are managed by the system.
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate(self, data):
        """
        OBJECT-LEVEL VALIDATION: Checks relationships between multiple fields.
        DRF Practice: Use this for logic that involves more than one field (like dates).
        """
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        # Support partial updates (PATCH) by fetching existing values if missing in payload
        if self.instance:
            if start_date is None:
                start_date = self.instance.start_date
            if end_date is None:
                end_date = self.instance.end_date

        if start_date and end_date and start_date >= end_date:
            raise serializers.ValidationError({
                "end_date": "End date must be after start date."
            })
        
        return data

    def validate_name(self, value):
        """
        FIELD-LEVEL VALIDATION: Checks a specific field.
        """
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty or just whitespace.")
        return value

    def validate_location(self, value):
        if not value.strip():
            raise serializers.ValidationError("Location cannot be empty or just whitespace.")
        return value
