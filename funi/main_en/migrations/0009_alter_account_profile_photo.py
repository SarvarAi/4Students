# Generated by Django 4.2.2 on 2023-06-25 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_en', '0008_account_schoolcertificates_maincertificates_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photo/'),
        ),
    ]