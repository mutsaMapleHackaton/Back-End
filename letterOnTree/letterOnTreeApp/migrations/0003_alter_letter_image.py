# Generated by Django 4.1.1 on 2022-11-18 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letterOnTreeApp', '0002_alter_letter_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img2'),
        ),
    ]
