# Generated by Django 3.1.12 on 2021-06-24 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[(None, 'Unknown'), ('Conservation', 'Conservation'), ('Reforestation', 'Reforestation')], max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('area_covered', models.IntegerField()),
                ('country', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('carbon_stored', models.IntegerField()),
                ('change_in_carbon_stored_in_last_30_days', models.IntegerField()),
            ],
        ),
    ]