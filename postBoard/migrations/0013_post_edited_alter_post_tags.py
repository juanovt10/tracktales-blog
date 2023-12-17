# Generated by Django 4.2.7 on 2023-12-12 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postBoard', '0012_contactinfo_submitted_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='edited',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(choices=[('', 'Holiday Type'), ('nightlife', 'Nightlife'), ('sightseeing', 'Sightseeing'), ('gastronomy', 'Gastronomy'), ('culture', 'Culture'), ('shopping', 'Shopping'), ('relaxation', 'Relaxation'), ('history', 'History'), ('adventure', 'Adventure'), ('stays', 'Stays'), ('nature', 'Nature'), ('festivals', 'Festivals'), ('beach', 'Beach')], default='sightseeing', max_length=50),
        ),
    ]