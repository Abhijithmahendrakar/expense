# Generated by Django 2.0 on 2019-05-23 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newitem',
            old_name='Created_at',
            new_name='created_at',
        ),
    ]
