from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'viewset', views.EventViewSet, basename='event-viewset')

urlpatterns = [
    # [MERGED]: Added home and about routes from Assignment-1
    path("home/", views.home),
    path("about/", views.about),
    
    # 1. FBV (Existing)
    path("create/", views.create_event),
    path("", views.get_all_events),
    path("<uuid:event_id>/", views.get_event),
    path("<uuid:event_id>/update/", views.update_event),
    path("<uuid:event_id>/delete/", views.delete_event),

    # 2. CBV (New)
    path("cbv/", views.EventListCBV.as_view(), name='event-list-cbv'),
    path("cbv/<uuid:event_id>/", views.EventDetailCBV.as_view(), name='event-detail-cbv'),

    # 3. Mixins (New)
    path("mixins/", views.EventMixinView.as_view(), name='event-mixin'),

    # 4. Generics (New)
    path("generics/", views.EventGenericListCreate.as_view(), name='event-generic-list'),
    path("generics/<uuid:id>/", views.EventGenericRetrieveUpdateDestroy.as_view(), name='event-generic-detail'),

    # 5. ViewSet (New)
    path("", include(router.urls)),
]
