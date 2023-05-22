from django.urls import path
from .views import feedback_detal_view, Feedback_view

urlpatterns = [
    path('', Feedback_view.as_view(), name='feedback'),
]
