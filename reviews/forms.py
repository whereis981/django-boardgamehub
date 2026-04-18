from django import forms
from .models import Review

class ReviewBaseForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('author', 'game', 'created_at', 'updated_at')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Review title'}),
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your review'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }
        labels = {
            'title': 'Title',
            'content': 'Review',
            'rating': 'Rating (1-5)',
        }

class ReviewCreateForm(ReviewBaseForm):
    pass

class ReviewEditForm(ReviewBaseForm):
    pass

class ReviewDeleteForm(ReviewBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
