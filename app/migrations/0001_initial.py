# Generated by Django 5.0.4 on 2024-04-15 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='app',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('icon', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=500)),
                ('discription', models.TextField()),
            ],
        ),
    ]
