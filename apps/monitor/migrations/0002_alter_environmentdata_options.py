# Generated by Django 3.2 on 2021-05-15 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='environmentdata',
            options={'ordering': ['-create_time'], 'verbose_name': '环境数据', 'verbose_name_plural': '环境数据'},
        ),
    ]
