# Generated by Django 5.0.1 on 2024-02-04 10:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Organization",
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
                ("org_name", models.CharField(max_length=50, unique=True)),
                (
                    "organization_category",
                    models.CharField(max_length=200, unique=True),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("username", models.CharField(max_length=20)),
                ("grade", models.CharField(max_length=10)),
                ("father_name", models.CharField(max_length=20)),
                ("Mother_name", models.CharField(max_length=20)),
                ("Permanent_address", models.CharField(max_length=20)),
                ("temporary_address", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Teacher",
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
                ("username", models.CharField(max_length=20)),
                ("subject", models.CharField(max_length=50)),
                ("Permanent_address", models.CharField(max_length=20)),
                ("temporary_address", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="InventoryItem",
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
                ("item_name", models.CharField(max_length=100)),
                ("item_code", models.CharField(max_length=10)),
                ("quantity", models.PositiveIntegerField()),
                ("category", models.CharField(max_length=50)),
                ("description", models.TextField()),
                (
                    "expiry_reminder",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "low_stock_reminder",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("purchase_date", models.DateField()),
                ("expiry_date", models.DateField()),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="montessori_app.organization",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Mark",
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
                ("subject", models.CharField(max_length=50)),
                ("score", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="montessori_app.student",
                    ),
                ),
                (
                    "checked_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="montessori_app.teacher",
                    ),
                ),
            ],
        ),
    ]
