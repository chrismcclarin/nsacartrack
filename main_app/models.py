from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django import forms

class Race(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'job_id': self.id})

class Racer(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date = models.DateField()