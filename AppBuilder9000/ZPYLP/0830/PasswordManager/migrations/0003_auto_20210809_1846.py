# Generated by Django 2.2.5 on 2021-08-09 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PasswordManager', '0002_auto_20210809_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpassword',
            name='type',
            field=models.CharField(choices=[('Personal', 'Personal'), ('Work', 'Work'), ('Combo', 'Combo'), ('Other', 'Other')], max_length=8),
        ),
    ]