# Generated by Django 2.0 on 2019-05-22 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField(null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]