# Generated by Django 4.2.2 on 2023-08-07 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_alter_camp_man_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camp',
            name='camp_id',
            field=models.CharField(max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name='camp',
            name='man_id',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]
