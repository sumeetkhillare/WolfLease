"""
    Altering field names in Owner and User Database 
"""

# Generated by Django 4.1.1 on 2022-10-08 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='contact_email',
            field=models.EmailField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact_email',
            field=models.EmailField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='flat_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='housing.flat'),
        ),
    ]
