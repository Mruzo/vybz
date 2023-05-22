from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404, reverse
from .models import Feedback, Comment
from django.views import generic

# Create your views here.


def feedback_detal_view(request, slug):
    obj = get_object_or_404(Feedback, slug=slug)
    template_name = ['vybz/feedback.html']
    context = {}
    context['object'] = obj
    context['meta'] = obj.as_meta()
    return render(request, template_name, context)


class Feedback_view(generic.ListView):
    model = Feedback
    template_name = "feedback/feedback.html"
    context_object_name = 'feedback'
    paginate_by = 4
