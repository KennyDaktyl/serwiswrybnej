# Generated by Django 4.2.13 on 2024-05-14 14:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (0, "Klient"),
                            (1, "Konto firmowe"),
                            (2, "Admin"),
                        ],
                        default=0,
                        verbose_name="Status",
                    ),
                ),
                (
                    "mobile",
                    models.CharField(
                        blank=True,
                        max_length=15,
                        null=True,
                        verbose_name="Mobile",
                    ),
                ),
                (
                    "company",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Nazwa firmy",
                    ),
                ),
                (
                    "nip",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        verbose_name="NIP",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Ulica",
                    ),
                ),
                (
                    "house_number",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        verbose_name="Numer domu",
                    ),
                ),
                (
                    "local_number",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        verbose_name="Numer lokalu",
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Miasto",
                    ),
                ),
                (
                    "postal_code",
                    models.CharField(
                        blank=True,
                        max_length=6,
                        null=True,
                        verbose_name="Kod pocztowy",
                    ),
                ),
                (
                    "inpost_code",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        verbose_name="Kod paczkomatu InPost",
                    ),
                ),
                (
                    "newsletter",
                    models.BooleanField(
                        default=False, verbose_name="Newsletter"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
        ),
    ]
