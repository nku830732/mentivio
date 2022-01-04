# Generated by Django 3.1.5 on 2022-01-01 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
        ('course', '0005_auto_20220101_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('Description', models.TextField(blank=True, max_length=500)),
                ('price', models.IntegerField(default=0)),
                ('designed_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='course.guider')),
                ('exam_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exam.exam')),
            ],
        ),
        migrations.CreateModel(
            name='MatterialTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=50)),
                ('materials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.materials')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=80000)),
                ('extra_resource', models.FileField(upload_to='media/guider/resources')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='course.materials')),
            ],
        ),
    ]
