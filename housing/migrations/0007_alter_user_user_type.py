# Generated by Django 5.1.2 on 2024-10-26 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("housing", "0006_alter_interested_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_type",
            field=models.CharField(
                choices=[("User", "User"), ("Owner", "Owner")],
                default="User",
                max_length=20,
            ),
        ),
    ]
