from django.db import models
import datetime
from django.contrib.auth.models import User


# Create your models here.
from django.urls import reverse


class Event(models.Model):
    author = models.ForeignKey(User, default=User, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="", null=True, blank=True)
    # date = models.DateField(default=datetime.date.day, editable=True, blank=True)
    date = models.DateField(editable=True, blank=True)
    done = models.BooleanField(default=False)
    # undone = models.BooleanField(default=True)

    class Meta:
        ordering = ["date"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('event', args=[str(self.id)])

    def get_author(self):
        return self.summary

    def __str__(self):
        return '%s, %s' % (self.summary, self.author)


