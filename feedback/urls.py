from django.urls import path
from .views import Feedback_view

urlpatterns = [
    path('feedback/<str:slug>/', Feedback_view.as_view(), name='feedback'),
    # path('', Comment_view.as_view, name='comment'),
]
