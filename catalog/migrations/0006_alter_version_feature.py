# Generated by Django 4.2.4 on 2023-09-23 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='feature',
            field=models.BooleanField(default=False, verbose_name='Признак текущей версии'),
        ),
    ]
