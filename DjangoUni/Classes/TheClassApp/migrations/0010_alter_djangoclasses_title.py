# Generated by Django 4.0.4 on 2022-05-03 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheClassApp', '0009_alter_djangoclasses_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='title',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
