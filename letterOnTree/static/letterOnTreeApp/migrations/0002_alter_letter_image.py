# Generated by Django 4.1.1 on 2022-11-18 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letterOnTreeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/img2'),
        ),
    ]
