# Generated by Django 3.1.2 on 2020-10-03 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_videourl'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='videolink',
            field=models.URLField(default='', max_length=250),
        ),
    ]