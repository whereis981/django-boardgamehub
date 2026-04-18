from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from games.models import BoardGame
from .forms import ReviewForm
from .models import Review

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review-create.html"

    def dispatch(self, request, *args, **kwargs):
        self.game = get_object_or_404(BoardGame, slug=self.kwargs["slug"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.game = self.game
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("game-details", kwargs={"slug": self.game.slug})
