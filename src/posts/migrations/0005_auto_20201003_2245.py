# Generated by Django 3.1.2 on 2020-10-03 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='videolink',
            field=models.URLField(default=False, max_length=250),
        ),
    ]
