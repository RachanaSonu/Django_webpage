# Generated by Django 4.2.7 on 2023-11-18 13:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_feedback1_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]