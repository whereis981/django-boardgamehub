from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from games.models import BoardGame

UserModel = get_user_model()


class Event(models.Model):
    organizer = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="organized_events")
    game = models.ForeignKey(BoardGame, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=150)
    date_time = models.DateTimeField()
    max_participants = models.PositiveIntegerField()
    participants = models.ManyToManyField(UserModel, related_name="joined_events", blank=True)
    is_public = models.BooleanField(default=True)

    def clean(self):
        if self.date_time <= timezone.now():
            raise ValidationError("Event date cannot be in the past.")
        if self.max_participants < 1:
            raise ValidationError("Max participants must be at least 1.")

    def __str__(self):
        return self.title
