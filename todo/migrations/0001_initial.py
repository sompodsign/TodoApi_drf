# Generated by Django 3.2.5 on 2021-07-23 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.IntegerField(max_length=9999)),
                ('title', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=10)),
                ('month', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=10)),
            ],
        ),
    ]
