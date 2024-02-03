# Generated by Django 5.0.1 on 2024-01-31 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_agent', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_estate', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=255)),
                ('zona', models.CharField(max_length=255)),
                ('total_mp', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('year_construction', models.IntegerField()),
                ('property_status', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
