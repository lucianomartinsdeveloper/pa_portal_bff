# Generated by Django 4.2 on 2023-06-20 10:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="type_of_audience",
            field=models.CharField(
                choices=[
                    ("MIG", "Migrando para a área de agilidade"),
                    ("PRO", "Profissional da área de agilidade"),
                    ("CUR", "Curioso sobre o universo da agilidade"),
                ],
                max_length=3,
                verbose_name="Tipo de público",
            ),
        ),
    ]
