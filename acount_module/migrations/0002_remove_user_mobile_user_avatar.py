# Generated by Django 5.1.3 on 2024-12-06 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acount_module', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mobile',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='تصویر آواتار'),
        ),
    ]
