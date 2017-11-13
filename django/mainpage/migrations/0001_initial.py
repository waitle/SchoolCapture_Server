# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 13:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='과목명', max_length=100)),
                ('teacher', models.CharField(default='담당선생님', max_length=10)),
                ('email', models.EmailField(default='이메일', max_length=50)),
                ('phone', models.CharField(default='연락처', max_length=13)),
                ('description', models.TextField(default='수행평가등을 메모하세요')),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='과목명', max_length=10)),
                ('start', models.TimeField()),
                ('term', models.TimeField()),
                ('end', models.TimeField()),
                ('Tset', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='auth',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.User'),
        ),
    ]