# Generated by Django 4.2.7 on 2023-11-18 13:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_feedback_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
