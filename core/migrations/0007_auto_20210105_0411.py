# Generated by Django 3.1.5 on 2021-01-05 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210105_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
