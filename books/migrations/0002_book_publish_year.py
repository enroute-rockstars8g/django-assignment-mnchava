# Generated by Django 4.0.3 on 2022-04-02 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publish_year',
            field=models.SmallIntegerField(default=2000),
        ),
    ]