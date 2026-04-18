from django import forms
from .models import Event

class EventBaseForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ["organizer"]

class EventCreateForm(EventBaseForm):
    pass

class EventEditForm(EventBaseForm):
    pass

class EventDeleteForm(EventBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
