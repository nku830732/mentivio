# Generated by Django 3.1.5 on 2021-12-24 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_guider_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='standard',
            field=models.IntegerField(null=True),
        ),
    ]
