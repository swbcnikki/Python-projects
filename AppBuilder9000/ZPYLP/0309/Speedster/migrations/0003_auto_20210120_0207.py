# Generated by Django 2.2.5 on 2021-01-20 09:07

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Speedster', '0002_auto_20210120_0101'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='vehicle',
            managers=[
                ('Vehicle', django.db.models.manager.Manager()),
            ],
        ),
    ]
