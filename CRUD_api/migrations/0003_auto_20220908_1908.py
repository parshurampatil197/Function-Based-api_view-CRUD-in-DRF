# Generated by Django 2.2 on 2022-09-08 19:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_api', '0002_auto_20220902_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='items',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]