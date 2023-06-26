from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=200)),
                ('last_name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
            ],
            managers=[
                ('User', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='WebScrape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[(None, 'Select Category'), ('Electronics', 'Electronics'), ('Pet Supplies', 'Pet Supplies'), ('Vehicles', 'Vehicles')], max_length=50)),
                ('url', models.URLField(default='')),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('imageUrl', models.URLField()),
                ('profit', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
            managers=[
                ('WebScrape_db', django.db.models.manager.Manager()),
            ],
        ),
    ]
