# Generated by Django 4.2.7 on 2023-12-27 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postBoard', '0013_post_edited_alter_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='approved',
        ),
    ]
