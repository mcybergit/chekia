# Generated by Django 4.0.1 on 2022-05-05 17:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=250)),
                ('phone', models.IntegerField(max_length=11)),
                ('national_number', models.CharField(max_length=10)),
                ('addres', models.CharField(blank=True, max_length=1000, null=True)),
                ('customer', models.BooleanField(default=False)),
                ('guarantor', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('last_edite_time', models.DateTimeField(blank=True, null=True)),
                ('delete_time', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.stors')),
            ],
        ),
    ]
