# Generated by Django 2.2.7 on 2019-11-20 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='short_link',
            field=models.CharField(max_length=250, unique=True, verbose_name='Сокращенная ссылка'),
        ),
    ]