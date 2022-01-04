# Generated by Django 3.2.6 on 2022-01-02 16:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_auto_20220102_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='AppointmentDate',
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointmentDates',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='appointmentDates'),
            preserve_default=False,
        ),
    ]
