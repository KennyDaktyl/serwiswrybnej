# Generated by Django 5.0.6 on 2024-06-24 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0016_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="main",
            field=models.BooleanField(
                default=False, verbose_name="Czy kategoria główna"
            ),
        ),
    ]