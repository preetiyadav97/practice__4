# Generated by Django 4.2.3 on 2023-07-31 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('Coursename', models.CharField(max_length=30)),
                ('Code', models.IntegerField(primary_key=3, serialize=False)),
                ('Collage', models.CharField(max_length=28)),
                ('Student', models.CharField(max_length=20)),
            ],
        ),
    ]
