from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    """Usuario de Django con un rol adicional para la aplicación."""

    ROL_CHOICES = (
        ('admin', 'Administrador'),
        ('cliente', 'Cliente'),
    )
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default='cliente')

    def es_admin(self) -> bool:
        """Indica si el usuario es administrador o superusuario."""
        return self.rol == 'admin' or self.is_superuser
