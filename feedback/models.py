from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL


class Feedback(models.Model):
    user_name = models.ForeignKey(
        User, default="vybz", null=True, on_delete=models.SET_NULL)
    summary = models.CharField(max_length=120)
    description = models.TextField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        # save model in order to get the id
        super(Feedback, self).save(*args, **kwargs)

        # then implement the logic for slug
        if not self.slug:
            self.slug = str(self.id)


class Comment(models.Model):
    user_name = models.ForeignKey(
        User, default="vybz", null=True, on_delete=models.SET_NULL)
    comment_cont = models.TextField(max_length=120, verbose_name='Comment')
    feedback = models.ForeignKey(
        Feedback, on_delete=models.CASCADE, related_name='feedback')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
