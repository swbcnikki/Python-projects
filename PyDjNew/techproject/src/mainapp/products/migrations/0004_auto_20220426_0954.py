# Generated by Django 2.1.5 on 2022-04-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220426_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('appetizers', 'appetizers'), ('drinks', 'drinks'), ('entrees', 'entrees')], max_length=60),
        ),
    ]