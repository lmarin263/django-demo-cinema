# Generated by Django 3.0.5 on 2020-06-14 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0005_auto_20200614_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditorium',
            name='seat_number',
            field=models.PositiveIntegerField(default=1),
        ),
    ]