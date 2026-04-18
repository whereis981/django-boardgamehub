from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Avg

from .forms import BoardGameCreateForm, BoardGameEditForm, BoardGameDeleteForm
from .models import BoardGame


class OwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class BoardGameListView(ListView):
    model = BoardGame
    template_name = 'games/game-list.html'
    context_object_name = 'games'
    paginate_by = 10


class BoardGameDetailView(DetailView):
    model = BoardGame
    template_name = 'games/game-details.html'
    context_object_name = 'game'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        avg = self.object.reviews.aggregate(avg_rating=Avg('rating'))
        context['average_rating'] = avg['avg_rating']
        return context


class BoardGameCreateView(LoginRequiredMixin, CreateView):
    model = BoardGame
    form_class = BoardGameCreateForm
    template_name = 'games/game-create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BoardGameEditView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = BoardGame
    form_class = BoardGameEditForm
    template_name = 'games/game-edit.html'


class BoardGameDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = BoardGame
    form_class = BoardGameDeleteForm
    template_name = 'games/game-delete.html'
    success_url = reverse_lazy('game-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BoardGameDeleteForm(instance=self.object)
        return context
