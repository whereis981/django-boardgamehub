from django.urls import path

from .views import RegisterView, AppLoginView, AppLogoutView, ProfileDetailView, ProfileEditView, redirect_to_own_profile

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', AppLoginView.as_view(), name='login'),
    path('logout/', AppLogoutView.as_view(), name='logout'),
    path('profile/', redirect_to_own_profile, name='my-profile'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-details'),
    path('profile/<int:pk>/edit/', ProfileEditView.as_view(), name='profile-edit'),
]
