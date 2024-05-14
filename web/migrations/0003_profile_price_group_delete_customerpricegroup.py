# Generated by Django 4.2.13 on 2024-05-14 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0002_pricegroup_product_alter_profile_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="price_group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="web.pricegroup",
            ),
        ),
        migrations.DeleteModel(
            name="CustomerPriceGroup",
        ),
    ]
