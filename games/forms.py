from django import forms

from .models import BoardGame


class BoardGameBaseForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        exclude = ('owner', 'slug', 'created_at', 'updated_at')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter game title'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe the board game'}),
            'year_published': forms.NumberInput(attrs={'placeholder': 'e.g. 2024'}),
            'min_players': forms.NumberInput(attrs={'placeholder': 'Minimum players'}),
            'max_players': forms.NumberInput(attrs={'placeholder': 'Maximum players'}),
            'play_time': forms.NumberInput(attrs={'placeholder': 'Minutes'}),
            'complexity': forms.NumberInput(attrs={'step': '0.1', 'placeholder': '1.0 - 5.0'}),
        }
        labels = {
            'title': 'Title',
            'description': 'Description',
            'year_published': 'Year Published',
            'min_players': 'Minimum Players',
            'max_players': 'Maximum Players',
            'play_time': 'Play Time',
            'complexity': 'Complexity',
            'image': 'Game Image',
            'categories': 'Categories',
            'mechanics': 'Mechanics',
        }
        help_texts = {
            'complexity': 'Use values like 1.0 to 5.0.',
            'play_time': 'Estimated duration in minutes.',
        }

    def clean_year_published(self):
        year = self.cleaned_data['year_published']
        if year < 1900 or year > 2100:
            raise forms.ValidationError('Year published must be between 1900 and 2100.')
        return year

    def clean(self):
        cleaned_data = super().clean()
        min_players = cleaned_data.get('min_players')
        max_players = cleaned_data.get('max_players')
        if min_players and max_players and min_players > max_players:
            raise forms.ValidationError('Minimum players cannot be greater than maximum players.')
        return cleaned_data


class BoardGameCreateForm(BoardGameBaseForm):
    pass


class BoardGameEditForm(BoardGameBaseForm):
    pass


class BoardGameDeleteForm(BoardGameBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
