# Generated by Django 5.1.1 on 2024-10-10 12:19

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_meetings_duration_meetings_start_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('start_time', models.TimeField(default=datetime.time(9, 0))),
                ('duration', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('floor', models.IntegerField()),
                ('room_number', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Meetings',
        ),
        migrations.AddField(
            model_name='meeting',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetings.room'),
        ),
    ]
