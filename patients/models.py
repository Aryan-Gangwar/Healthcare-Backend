from django.conf import settings
from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    address = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,        # 👈 allow nulls
        blank=True        # 👈 allow empty in forms
    )

    def __str__(self):
        return self.name
