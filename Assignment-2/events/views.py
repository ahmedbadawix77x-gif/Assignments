from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer


@api_view(['POST'])
def create_event(request):
    """
    Brings a new event into existence using DRF Serializer.
    This replaces manual JSON parsing and manual validation loops.
    """
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Event created", 
            "id": str(serializer.instance.id)
        }, status=status.HTTP_201_CREATED)
    
    # serializer.errors automatically provides detailed field-level error messages
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_events(request):
    """
    Reveals all events using DRF Serializer.
    """
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_event(request, event_id):
    """
    Focuses on a single event using DRF Serializer.
    """
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = EventSerializer(event)
    return Response(serializer.data)


@api_view(['PATCH'])
def update_event(request, event_id):
    """
    Alters the details of an existing event using DRF Serializer.
    partial=True allows us to update only the fields sent in the request.
    """
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = EventSerializer(event, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Event updated"})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_event(request, event_id):
    """
    Makes an event disappear.
    """
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

    event.delete()
    return Response({"message": "Event deleted"})



def home(request):

    from django.http import HttpResponse
    return HttpResponse("welcome to home page")


def about(request):

    from django.http import HttpResponse
    return HttpResponse("welcome to about page")
