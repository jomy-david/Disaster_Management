# Generated by Django 4.2.2 on 2023-08-08 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_alter_camp_camp_id_alter_camp_man_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='curr_capacity',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='camp',
            name='total_capacity',
            field=models.PositiveIntegerField(default=100),
            preserve_default=False,
        ),
    ]
