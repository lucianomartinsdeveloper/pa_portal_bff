# Generated by Django 4.2 on 2023-06-27 13:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_remove_user_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=150, verbose_name="Nome"),
        ),
    ]
