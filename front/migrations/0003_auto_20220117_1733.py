# Generated by Django 3.2 on 2022-01-17 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_auto_20220117_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListThings',
            fields=[
                ('things_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('process', models.IntegerField()),
                ('emotion', models.IntegerField()),
                ('energy', models.IntegerField()),
                ('key', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.TextField(max_length=32, unique=True)),
                ('user_passwd', models.TextField(max_length=32)),
            ],
        ),
        migrations.RemoveField(
            model_name='energy',
            name='things_date',
        ),
        migrations.RemoveField(
            model_name='process',
            name='things_date',
        ),
        migrations.DeleteModel(
            name='emotion',
        ),
        migrations.DeleteModel(
            name='energy',
        ),
        migrations.DeleteModel(
            name='process',
        ),
        migrations.DeleteModel(
            name='Things_Date',
        ),
        migrations.AddField(
            model_name='listthings',
            name='user_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='front.user'),
        ),
    ]
