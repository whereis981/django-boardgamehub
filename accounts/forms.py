from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='Email address',
        help_text='Enter a valid email address.',
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Choose username'}),
        }
        labels = {
            'username': 'Username',
        }
        help_texts = {
            'username': 'Use letters, numbers, and @/./+/-/_ only.',
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserModel.objects.filter(email=email).exists():
            raise forms.ValidationError('An account with this email already exists.')
        return email


class AppAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'city', 'favorite_genre', 'birth_date', 'avatar')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us about yourself'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter your city'}),
            'favorite_genre': forms.TextInput(attrs={'placeholder': 'Favorite board game genre'}),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'bio': 'Biography',
            'city': 'City',
            'favorite_genre': 'Favorite Genre',
            'birth_date': 'Birth Date',
            'avatar': 'Profile Image',
        }

    def clean_city(self):
        city = self.cleaned_data['city']
        if city and len(city) < 2:
            raise forms.ValidationError('City must contain at least 2 characters.')
        return city
