# Generated by Django 4.2.7 on 2023-12-08 13:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('postBoard', '0011_contactinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='submitted_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
