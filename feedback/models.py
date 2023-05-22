from django.db import models

# Create your models here.


class Feedback(models.Model):
    summary = models.CharField(max_length=120)
    description = models.TextField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.summary

    def save(self, *args, **kwargs):
        # save model in order to get the id
        super(Feedback, self).save(*args, **kwargs)

        # then implement the logic for slug
        if not self.slug:
            self.slug = str(self.id)


class Comment(models.Model):
    comment_cont = models.TextField(max_length=120, verbose_name='Comment')
    feedback = models.ForeignKey(
        Feedback, on_delete=models.CASCADE, related_name='feedback')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
