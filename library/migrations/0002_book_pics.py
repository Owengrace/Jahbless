# Generated by Django 2.1.2 on 2019-01-01 10:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pics',
            field=models.ImageField(default=django.utils.timezone.now, height_field='50px', max_length=200, upload_to=None, width_field='45px'),
            preserve_default=False,
        ),
    ]
