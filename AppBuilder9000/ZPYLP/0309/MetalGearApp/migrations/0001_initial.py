# Generated by Django 3.1.4 on 2021-01-10 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiamondDogList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=20)),
                ('lName', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Prefer not to say ', 'Prefer not to say')], max_length=30)),
                ('specialization', models.CharField(choices=[('Research And Development', 'Research and Development'), ('Intel', 'Intel'), ('Command', 'Command'), ('Combat', 'Combat'), ('Medical', 'Medical'), ('Base Development', 'Base Development'), ('Support', 'Support'), ('Animal Conservation', 'Animal Conservation')], max_length=50)),
                ('codePrefix', models.CharField(choices=[('Solid', 'Solid'), ('Liquid', 'Liquid'), ('Solidus', 'Solidus'), ('Charging', 'Charging'), ('Psycho', 'Psycho'), ('Arsenal', 'Arsenal'), ('Revolver', 'Revolver'), ('Killer', 'Killer'), ('White', 'White'), ('Black', 'Black'), ('Screaming', 'Screaming'), ('Raging', 'Raging'), ('Crying', 'Crying'), ('Decoy', 'Decoy'), ('Sniper', 'Sniper')], max_length=30)),
                ('codeSuffix', models.CharField(choices=[('Wolf', 'Wolf'), ('Snake', 'Snake'), ('Mantis', 'Mantis'), ('Raven', 'Raven'), ('Rhino', 'Rhino'), ('Ocelot', 'Ocelot'), ('Tiger', 'Tiger'), ('Shark', 'Shark'), ('Fox', 'Fox'), ('Panther', 'Panther'), ('Eagle', 'Eagle'), ('Jackal', 'Jackal'), ('Zebra', 'Zebra'), ('Deer', 'Deer'), ('Elephant', 'Elephant'), ('Hippopotamus', 'Hippopotamus'), ('Turtle', 'Turtle'), ('Chicken', 'Chicken')], max_length=50)),
                ('email', models.EmailField(blank=True, default='', max_length=100)),
            ],
        ),
    ]