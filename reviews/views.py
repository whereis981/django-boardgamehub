from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from games.models import BoardGame
from .forms import ReviewCreateForm, ReviewEditForm, ReviewDeleteForm
from .models import Review

class ReviewOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        return self.get_object().author == self.request.user

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewCreateForm
    template_name = 'reviews/review-create.html'

    def dispatch(self, request, *args, **kwargs):
        self.game = get_object_or_404(BoardGame, slug=self.kwargs['slug'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.game = self.game
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('game-details', kwargs={'slug': self.game.slug})

class ReviewEditView(LoginRequiredMixin, ReviewOwnerMixin, UpdateView):
    model = Review
    form_class = ReviewEditForm
    template_name = 'reviews/review-edit.html'

    def get_success_url(self):
        return reverse_lazy('game-details', kwargs={'slug': self.object.game.slug})

class ReviewDeleteView(LoginRequiredMixin, ReviewOwnerMixin, DeleteView):
    model = Review
    form_class = ReviewDeleteForm
    template_name = 'reviews/review-delete.html'

    def get_success_url(self):
        return reverse_lazy('game-details', kwargs={'slug': self.object.game.slug})
