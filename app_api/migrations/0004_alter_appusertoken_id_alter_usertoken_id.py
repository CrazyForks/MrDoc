# Generated by Django 4.2.16 on 2024-10-17 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0003_appusertoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appusertoken',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='usertoken',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
