# Generated by Django 2.2.28 on 2022-07-12 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0055_pytz_2022_2_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulingevent',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='When the event happened'),
        ),
    ]