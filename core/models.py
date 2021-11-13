# Custom User
from django.contrib.auth.models import AbstractUser

# App Models
from django.db import models

# Timezone
from django.utils import timezone

# Module for generate password
import uuid


class User(AbstractUser):
    pass


class Base(models.Model):
    """Model Base that repeat in all models"""
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Client(Base):
    """Model Client
        user, email, birth date and password
        
        * password is not mandatory but when no value is entered, a random password will be generated.
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="User")
    email = models.EmailField(max_length=150, verbose_name="Email")
    birth_date = models.DateField(default=timezone.now)
    password = models.CharField(max_length=20, verbose_name="Senha", blank=True)

    class Meta:
        ordering = ('-email',)
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.password == '':
            self.password = f"{uuid.uuid4}"
        super().save(*args, **kwargs)

    def to_dict_json(self):
        return {
            'pk':self.pk,
            'user':self.user,
            'email':self.email,
            'birth_date': self.birth_date,
            'password': self.password,
        }        