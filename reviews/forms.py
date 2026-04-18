from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["title", "content", "rating"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Review title"}),
            "content": forms.Textarea(attrs={"rows": 4}),
            "rating": forms.NumberInput(attrs={"min": 1, "max": 5}),
        }
