# Generated by Django 2.2.7 on 2019-11-12 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191112_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account_type',
            field=models.CharField(choices=[('Полный пакет', 'full'), ('Бесплатный пакет', 'free')], default='Бесплатный пакет', max_length=30),
        ),
    ]
