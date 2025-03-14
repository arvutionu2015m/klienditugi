from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = [
    ('open', 'Avatud'),
    ('in_progress', 'Töös'),
    ('resolved', 'Lahendatud'),
    ('closed', 'Suletud'),
]

PRIORITY_CHOICES = [
    ('low', 'Madal'),
    ('medium', 'Keskmine'),
    ('high', 'Kõrge'),
    ('urgent', 'Kiireloomuline'),
]

class ResponseTemplate(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.title


class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subject} ({self.get_status_display()})"
