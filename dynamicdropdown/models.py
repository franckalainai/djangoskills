from django.db import models
from django.utils import timezone


class Subject(models.Model):
    subject_id = models.CharField(max_length=250, blank=True)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Topic(models.Model):
    topic_id = models.CharField(max_length=250, blank=True)
    title = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title