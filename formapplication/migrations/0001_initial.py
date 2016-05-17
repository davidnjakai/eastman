# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patid', models.IntegerField(default=0)),
                ('lastname', models.CharField(max_length=45)),
                ('firstname', models.CharField(max_length=45)),
                ('middlename', models.CharField(max_length=45)),
                ('title', models.CharField(max_length=45)),
                ('mobilenumber', models.CharField(max_length=45)),
                ('mobilenumber2', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('guarantor', models.IntegerField(default=0)),
                ('dateofbirth', models.DateField()),
                ('filenumber', models.IntegerField(default=0)),
                ('photolocation', models.CharField(max_length=45)),
                ('gender', models.CharField(max_length=10)),
                ('position', models.CharField(max_length=10)),
                ('dueamount', models.IntegerField(default=0)),
                ('insuranceamount', models.IntegerField(default=0)),
                ('balancedue', models.IntegerField(default=0)),
                ('occupation', models.CharField(max_length=45)),
                ('employer_school', models.CharField(max_length=45)),
            ],
        ),
    ]