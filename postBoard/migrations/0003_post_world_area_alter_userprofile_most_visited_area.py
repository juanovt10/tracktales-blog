# Generated by Django 4.2.7 on 2023-11-26 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postBoard', '0002_userprofile_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='world_area',
            field=models.CharField(choices=[('north_america', 'North America'), ('south_america', 'South America'), ('europe', 'Europe'), ('south_asia', 'South Asia'), ('east_asia', 'East Asia'), ('west_asia', 'West Asia'), ('oceania', 'Oceania'), ('africa', 'Africa'), ('middle_east', 'Middle East')], default='europe', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='most_visited_area',
            field=models.CharField(choices=[('north_america', 'North America'), ('south_america', 'South America'), ('europe', 'Europe'), ('south_asia', 'South Asia'), ('east_asia', 'East Asia'), ('west_asia', 'West Asia'), ('oceania', 'Oceania'), ('africa', 'Africa'), ('middle_east', 'Middle East')], max_length=50),
        ),
    ]
