# Generated by Django 3.1.2 on 2020-10-03 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20201003_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='videolink',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]