from django.contrib import admin
from .models import BoardGame, Category, Mechanic, CollectionEntry, Favorite

admin.site.register(BoardGame)
admin.site.register(Category)
admin.site.register(Mechanic)
admin.site.register(CollectionEntry)
admin.site.register(Favorite)
