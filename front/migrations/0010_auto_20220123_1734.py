# Generated by Django 3.2 on 2022-01-23 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0009_alter_listthings_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ListThings',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]