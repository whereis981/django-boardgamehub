from django.urls import path
from .views import ReviewCreateView

urlpatterns = [
    path("create/<slug:slug>/", ReviewCreateView.as_view(), name="review-create"),
]
