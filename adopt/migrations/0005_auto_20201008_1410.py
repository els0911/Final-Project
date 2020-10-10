# Generated by Django 3.1.2 on 2020-10-08 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopt', '0004_pet_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='profile_image',
            field=models.ImageField(blank=True, help_text='Profile picture of a pet', upload_to='profile_images'),
        ),
    ]
