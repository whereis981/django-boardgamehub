from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import AppUserCreationForm, AppAuthenticationForm, ProfileEditForm
from .models import Profile

UserModel = get_user_model()


class RegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class AppLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = AppAuthenticationForm


class AppLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile-details.html'
    context_object_name = 'profile'


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


def redirect_to_own_profile(request):
    return redirect('profile-details', pk=request.user.profile.pk)
