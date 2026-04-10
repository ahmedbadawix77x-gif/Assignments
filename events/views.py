from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, views, generics, mixins, viewsets
from .models import Event
from .serializers import EventSerializer


# =========================================
# 1. FBV (Function-Based Views)
# ==========================================

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


# ==========================================
# 2. CBV (Class-Based Views - APIView)
# =========================================
class EventListCBV(views.APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetailCBV(views.APIView):
    def get_object(self, event_id):
        try:
            return Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return None

    def get(self, request, event_id):
        event = self.get_object(event_id)
        if not event:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def patch(self, request, event_id):
        event = self.get_object(event_id)
        if not event:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EventSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, event_id):
        event = self.get_object(event_id)
        if not event:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ==========================================
# 3. Mixins
# ==========================================
class EventMixinView(generics.GenericAPIView, 
                    mixins.ListModelMixin, 
                    mixins.CreateModelMixin):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# ==========================================
# 4. Generics
# ==========================================
class EventGenericListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventGenericRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'id'


# ==========================================
# 5. ViewSet
# ==========================================
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer



def home(request):

    from django.http import HttpResponse
    return HttpResponse("welcome to home page")


def about(request):

    from django.http import HttpResponse
    return HttpResponse("welcome to about page")
