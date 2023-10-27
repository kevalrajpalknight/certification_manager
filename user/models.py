from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext as _

from .managers import UserManager


numeric_validator = RegexValidator(
    regex=r"^[0-9]*$",
    message=_("Phone number must contain only numeric characters."),
    code="invalid_phone",
)


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    name = models.CharField(
        verbose_name=_("Full Name"),
        max_length=50,
        null=False,
        blank=False,
        db_column="name",
    )
    email = models.EmailField(
        _("Email Address"),
        unique=True,
        null=False,
        blank=False,
        db_column="email",
    )
    phone = models.CharField(
        verbose_name=_("Phone Number"),
        db_column="phone",
        max_length=10,
        validators=[numeric_validator],
    )
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        if self.name:
            return self.name
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Manage Users"
        db_table = "User"

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["email"]),
            models.Index(fields=["phone"]),
        ]
