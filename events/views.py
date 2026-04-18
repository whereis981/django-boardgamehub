from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import EventCreateForm, EventEditForm, EventDeleteForm
from .models import Event

class EventOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object().organizer == self.request.user

class EventListView(ListView):
    model = Event
    template_name = "events/event-list.html"
    context_object_name = "events"

class EventDetailView(DetailView):
    model = Event
    template_name = "events/event-details.html"
    context_object_name = "event"

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventCreateForm
    template_name = "events/event-create.html"

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)

class EventEditView(LoginRequiredMixin, EventOwnerMixin, UpdateView):
    model = Event
    form_class = EventEditForm
    template_name = "events/event-edit.html"

class EventDeleteView(LoginRequiredMixin, EventOwnerMixin, DeleteView):
    model = Event
    form_class = EventDeleteForm
    template_name = "events/event-delete.html"
    success_url = reverse_lazy("event-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = EventDeleteForm(instance=self.object)
        return context
