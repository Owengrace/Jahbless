# Generated by Django 2.1.2 on 2019-01-01 14:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20190101_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='picss',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='file:///C:/Users/Jahbless/Pictures/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='pic',
            field=models.ImageField(upload_to=None),
        ),
    ]