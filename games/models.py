from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify

UserModel = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Mechanic(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class BoardGame(models.Model):
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="owned_games")
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    year_published = models.PositiveIntegerField()
    min_players = models.PositiveIntegerField()
    max_players = models.PositiveIntegerField()
    play_time = models.PositiveIntegerField(help_text="Duration in minutes")
    complexity = models.DecimalField(max_digits=3, decimal_places=1)
    image = models.ImageField(upload_to="games/", null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name="games")
    mechanics = models.ManyToManyField(Mechanic, related_name="games")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.min_players > self.max_players:
            raise ValidationError("Minimum players cannot be greater than maximum players.")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class CollectionEntry(models.Model):
    STATUS_CHOICES = [
        ("Owned", "Owned"),
        ("Wishlist", "Wishlist"),
        ("Played", "Played"),
        ("Trading", "Trading"),
    ]

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="collection_entries")
    game = models.ForeignKey(BoardGame, on_delete=models.CASCADE, related_name="collection_entries")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    notes = models.TextField(blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.game.title} ({self.status})"


class Favorite(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="favorites")
    game = models.ForeignKey(BoardGame, on_delete=models.CASCADE, related_name="favorited_by")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "game"], name="unique_user_game_favorite")
        ]

    def __str__(self):
        return f"{self.user.username} likes {self.game.title}"
