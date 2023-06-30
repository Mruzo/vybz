from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404, reverse
from .models import Feedback, Comment
from django.views import generic

# Create your views here.


class Feedback_list(generic.ListView):
    model = Feedback
    template_name = "base.html"
    context_object_name = 'feedback_list'


class Feedback_view(generic.DetailView):
    model = Feedback
    template_name = "feedback/feedback.html"
    context_object_name = 'feedback'
    # paginate_by = 4

    def get_object(self, queryset=None):
        # Retrieve the specific feedback object based on it's ID
        return get_object_or_404(Feedback, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        feedback = self.get_object()
        context['images'] = feedback.images.all()
        context['comments'] = feedback.comments.all()
        return context


# class Comment_view(generic.ListView):
#     model = Comment
#     template_name = "feedback/.html"
#     context_object_name = 'user_comment'
