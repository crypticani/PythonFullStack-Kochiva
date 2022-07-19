# Generated by Django 4.0.1 on 2022-07-19 03:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('content', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='footers/')),
            ],
            options={
                'verbose_name_plural': 'Footers',
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('content', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='headers/')),
            ],
            options={
                'verbose_name_plural': 'Headers',
            },
        ),
        migrations.CreateModel(
            name='EmailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_to', models.EmailField(max_length=254)),
                ('cc', models.EmailField(blank=True, max_length=254, null=True)),
                ('bcc', models.EmailField(blank=True, max_length=254, null=True)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=250)),
                ('file', models.FileField(upload_to='files/')),
                ('status', models.CharField(choices=[('queued', 'queued'), ('sent', 'sent'), ('failed', 'failed')], default='queued', max_length=50)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 7, 19, 9, 21, 30, 760917))),
                ('sent_at', models.DateTimeField(blank=True, null=True)),
                ('footer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='TaskQueues.footer')),
                ('header', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='TaskQueues.header')),
            ],
            options={
                'verbose_name_plural': 'Emails',
            },
        ),
    ]