from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404, reverse
from .models import Feedback, Comment
from django.views import generic

# Create your views here.


# def feedback_detal_view(request, slug):
#     obj = get_object_or_404(Feedback, slug=slug)
#     template_name = ['vybz/feedback.html']
#     context = {}
#     context['object'] = obj
#     context['meta'] = obj.as_meta()
#     return render(request, template_name, context)


class Feedback_view(generic.DetailView):
    model = Feedback
    template_name = "feedback/feedback.html"
    context_object_name = 'feedback'
    # paginate_by = 4

    def get_object(self, queryset=None):
        # Retrieve the specific feedback object based on iths ID
        return get_object_or_404(Feedback, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        feedback = self.get_object()
        context['comments'] = feedback.comments.all()
        return context


# class Comment_view(generic.ListView):
#     model = Comment
#     template_name = "feedback/.html"
#     context_object_name = 'user_comment'
