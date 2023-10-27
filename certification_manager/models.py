from django.db import models
from django.utils.translation import gettext as _

from django.contrib.auth import get_user_model


class Address(models.Model):
    local_address = models.CharField(
        verbose_name=_("Local Address"), db_column="local_address", max_length=255
    )
    city = models.CharField(verbose_name=_("City"), db_column="city", max_length=100)
    user = models.OneToOneField(
        get_user_model(),
        verbose_name=_("User"),
        db_column="user",
        on_delete=models.CASCADE,
        related_name="address",
    )

    class Meta:
        indexes = [
            models.Index(fields=["local_address"]),
            models.Index(fields=["city"]),
        ]
        db_table = "address"


class Certifications(models.Model):
    certificate_name = models.CharField(
        verbose_name=_("Certificate Name"), db_column="certificate_name", max_length=255
    )
    duration = models.PositiveIntegerField(
        verbose_name=_("Duration"), db_column="duration"
    )
    user = models.ForeignKey(
        get_user_model(),
        verbose_name=_("User"),
        db_column="user",
        on_delete=models.CASCADE,
        related_name="certifications",
    )

    class Meta:
        indexes = [
            models.Index(fields=["certificate_name"]),
        ]
        db_table = "certifications"


class Profession(models.Model):
    profession = models.CharField(
        verbose_name=_("Profession"), db_column="profession", max_length=255
    )
    user = models.ForeignKey(
        get_user_model(),
        verbose_name=_("User"),
        db_column="user",
        on_delete=models.CASCADE,
        related_name="profession",
    )

    def __str__(self):
        return self.profession

    class Meta:
        indexes = [
            models.Index(fields=["profession"]),
        ]
        db_table = "profession"
