from django.urls import path

from .views import BoardGameListView, BoardGameDetailView, BoardGameCreateView, BoardGameEditView, BoardGameDeleteView

urlpatterns = [
    path('', BoardGameListView.as_view(), name='game-list'),
    path('create/', BoardGameCreateView.as_view(), name='game-create'),
    path('<slug:slug>/', BoardGameDetailView.as_view(), name='game-details'),
    path('<slug:slug>/edit/', BoardGameEditView.as_view(), name='game-edit'),
    path('<slug:slug>/delete/', BoardGameDeleteView.as_view(), name='game-delete'),
]
