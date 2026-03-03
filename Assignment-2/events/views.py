import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Event


# create_event – The Summoning Spell
# Brings a new event into existence.
@csrf_exempt
def create_event(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)
    
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    # Basic validation
    required_fields = ["name", "description", "location", "start_date", "end_date"]
    for field in required_fields:
        if not data.get(field):
            return JsonResponse({"error": f"Field '{field}' is required"}, status=400)

    event = Event.objects.create(
        name=data.get("name"),
        description=data.get("description"),
        location=data.get("location"),
        start_date=data.get("start_date"),
        end_date=data.get("end_date"),
    )

    return JsonResponse({"message": "Event created", "id": str(event.id)}, status=201)


# get_all_events – The Scrying Spell
# Reveals all events.
def get_all_events(request):
    if request.method != "GET":
        return JsonResponse({"error": "Only GET method is allowed"}, status=405)
    
    events = list(Event.objects.values())
    return JsonResponse(events, safe=False)


# get_event – The Lens Spell
# Focuses on a single event.
def get_event(request, event_id):
    if request.method != "GET":
        return JsonResponse({"error": "Only GET method is allowed"}, status=405)

    # Using try/except instead of get_object_or_404
    # to return JSON response instead of default HTML 404 page

    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return JsonResponse({"error": "Event not found"}, status=404)

    return JsonResponse({
        "id": str(event.id),
        "name": event.name,
        "description": event.description,
        "location": event.location,
        "start_date": event.start_date,
        "end_date": event.end_date,
    })

# update_event – The Transforming Spell
# Alters the details of an existing event.
@csrf_exempt
def update_event(request, event_id):
    if request.method != "PATCH":
        return JsonResponse({"error": "Only PATCH method is allowed"}, status=405)

    # Handling object retrieval manually
    # to ensure consistent JSON API responses

    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return JsonResponse({"error": "Event not found"}, status=404)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    event.name = data.get("name", event.name)
    event.description = data.get("description", event.description)
    event.location = data.get("location", event.location)
    event.start_date = data.get("start_date", event.start_date)
    event.end_date = data.get("end_date", event.end_date)
    event.save()

    return JsonResponse({"message": "Event updated"})

# delete_event – The Vanishing Spell
# Makes an event disappear.
@csrf_exempt
def delete_event(request, event_id):
    if request.method != "DELETE":
        return JsonResponse({"error": "Only DELETE method is allowed"}, status=405)

    # Returning JSON 404 instead of Django's default HTML error page
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return JsonResponse({"error": "Event not found"}, status=404)

    event.delete()
    return JsonResponse({"message": "Event deleted"})