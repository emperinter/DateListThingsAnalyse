# Generated by Django 3.2 on 2022-01-17 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('background', '0008_alter_listthings_things_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listthings',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]
