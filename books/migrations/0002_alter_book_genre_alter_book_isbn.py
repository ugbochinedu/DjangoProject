# Generated by Django 4.2.4 on 2023-08-11 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('FICTION', 'Fiction'), ('FINANCE', 'Finance'), ('POLITICS', 'Politics'), ('ROMANCE', 'Romance')], default='Finance', max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=20),
        ),
    ]