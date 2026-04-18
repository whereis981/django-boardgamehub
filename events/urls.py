from django.urls import path
from .views import EventListView, EventDetailView, EventCreateView, EventEditView, EventDeleteView

urlpatterns = [
    path("", EventListView.as_view(), name="event-list"),
    path("create/", EventCreateView.as_view(), name="event-create"),
    path("<int:pk>/", EventDetailView.as_view(), name="event-details"),
    path("<int:pk>/edit/", EventEditView.as_view(), name="event-edit"),
    path("<int:pk>/delete/", EventDeleteView.as_view(), name="event-delete"),
]
