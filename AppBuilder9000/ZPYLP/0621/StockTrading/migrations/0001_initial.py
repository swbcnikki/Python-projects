# Generated by Django 2.2.5 on 2021-05-24 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(blank=True, max_length=10)),
                ('lName', models.CharField(blank=True, max_length=10)),
                ('article', models.TextField(blank=True, max_length=1000)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('tags', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
