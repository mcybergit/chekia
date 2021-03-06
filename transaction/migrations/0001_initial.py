# Generated by Django 4.0.1 on 2022-05-05 19:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        ('persons', '0002_alter_persons_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('last_edite_time', models.DateTimeField(blank=True, null=True)),
                ('receipt_time', models.DateTimeField(blank=True, null=True)),
                ('goods', models.CharField(blank=True, max_length=500, null=True)),
                ('amount', models.IntegerField()),
                ('profit', models.FloatField()),
                ('term', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=1500, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_transaction', to='persons.persons')),
                ('guarantor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='guarantor_transaction', to='persons.persons')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.stors')),
            ],
        ),
    ]
