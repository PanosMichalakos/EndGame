# Generated by Django 3.1.2 on 2020-10-03 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_videolink'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='review',
            field=models.BooleanField(default=False),
        ),
    ]