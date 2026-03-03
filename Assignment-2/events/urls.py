from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_event),
    path("", views.get_all_events),
    path("<uuid:event_id>/", views.get_event),
    path("<uuid:event_id>/update/", views.update_event),
    path("<uuid:event_id>/delete/", views.delete_event),
]