# Generated by Django 3.1.5 on 2021-12-19 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
        ('blog', '0002_strategyquesition_strategyquesitionreply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career_oppotunitie',
            name='exam_to_qualify',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.exam'),
        ),
    ]
