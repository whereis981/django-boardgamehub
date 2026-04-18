from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

from games.models import BoardGame

UserModel = get_user_model()


class Review(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="reviews")
    game = models.ForeignKey(BoardGame, on_delete=models.CASCADE, related_name="reviews")
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if not 1 <= self.rating <= 5:
            raise ValidationError("Rating must be between 1 and 5.")

    def __str__(self):
        return f"{self.title} - {self.game.title}"
