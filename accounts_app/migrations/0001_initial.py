# Generated by Django 3.2.6 on 2021-12-02 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=36, unique=True)),
                ('name', models.CharField(blank=True, max_length=36, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('password', models.CharField(max_length=36)),
            ],
        ),
    ]
