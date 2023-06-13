from django.urls import path
from .views import Feedback_list, Feedback_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('feedback/', Feedback_list.as_view(), name='feedback_list'),
    path('feedback/<str:slug>/', Feedback_view.as_view(), name='feedback'),
    # path('', Comment_view.as_view, name='comment'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
