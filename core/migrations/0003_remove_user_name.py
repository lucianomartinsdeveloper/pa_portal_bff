# Generated by Django 4.2 on 2023-06-21 10:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_alter_user_type_of_audience"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="name",
        ),
    ]
