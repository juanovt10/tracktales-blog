# Generated by Django 4.2.7 on 2023-11-27 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postBoard', '0003_post_world_area_alter_userprofile_most_visited_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='country',
            field=models.CharField(default='Enter Country', max_length=50),
        ),
    ]
