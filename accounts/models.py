from django.db import models
from django.contrib.auth.models import User


class Activation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='accounts_activation')
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
