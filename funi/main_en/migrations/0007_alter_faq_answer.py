# Generated by Django 4.2.2 on 2023-06-20 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_en', '0006_faq_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
    ]
