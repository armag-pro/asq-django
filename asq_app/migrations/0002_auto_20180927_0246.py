# Generated by Django 2.1.1 on 2018-09-26 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asq_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='profile_pic',
            field=models.ImageField(blank=True, default=0, upload_to=''),
        ),
    ]
