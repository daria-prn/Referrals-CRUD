# Generated by Django 3.0.8 on 2020-07-09 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid_cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]
