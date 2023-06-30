from django.contrib import admin
from .models import Feedback, FeedbackImage, Comment


# Register your models here.

admin.site.register(Feedback)
admin.site.register(FeedbackImage)
admin.site.register(Comment)
