# Generated by Django 3.1.4 on 2020-12-13 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ripple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, default='', max_length=70)),
                ('userid', models.CharField(blank=True, default='', max_length=70)),
                ('comment', models.CharField(blank=True, default='', max_length=70)),
                ('timestamp', models.CharField(blank=True, default='', max_length=70)),
            ],
        ),
    ]
