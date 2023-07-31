# Generated by Django 4.2.3 on 2023-07-31 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Coursename', models.CharField(max_length=30)),
                ('Code', models.IntegerField()),
                ('Collage', models.CharField(max_length=28)),
                ('Student', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]