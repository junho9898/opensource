# Generated by Django 3.0.6 on 2020-05-07 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('contents', models.TextField()),
                ('img', models.ImageField(upload_to='')),
                ('dataCreat', models.DateTimeField()),
                ('category', models.CharField(max_length=20)),
            ],
        ),
    ]
