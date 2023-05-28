from django.urls import path
from .views import Feedback_view, Comment_view

urlpatterns = [
    path('', Feedback_view.as_view(), name='feedback'),
    path('', Comment_view.as_view, name='comment'),
]
