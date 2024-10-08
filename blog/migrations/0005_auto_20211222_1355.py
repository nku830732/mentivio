# Generated by Django 3.1.5 on 2021-12-22 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogads'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogads',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='media/explore/'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='adsTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='enter the title of post to embed it', max_length=50)),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.blogads')),
            ],
        ),
    ]
