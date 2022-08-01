# Generated by Django 4.0.6 on 2022-08-01 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('borough', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cuisine', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=2)),
                ('rating', models.IntegerField(default=3)),
                ('comments', models.CharField(max_length=200)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurants.neighborhoods')),
            ],
        ),
    ]
