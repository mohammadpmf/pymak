# Generated by Django 4.0.5 on 2022-09-07 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('color', models.CharField(max_length=40)),
            ],
        ),
    ]
