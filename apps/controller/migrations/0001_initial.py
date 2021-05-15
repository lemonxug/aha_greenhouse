# Generated by Django 3.2 on 2021-05-13 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='指令名称')),
                ('path', models.CharField(max_length=100, verbose_name='路径')),
                ('parameter', models.CharField(max_length=100, verbose_name='参数')),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='monitor.device', verbose_name='设备名称')),
            ],
            options={
                'verbose_name': '设备指令表',
                'verbose_name_plural': '设备指令表',
            },
        ),
        migrations.CreateModel(
            name='TimerControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('stop_time', models.DateTimeField(verbose_name='结束时间')),
                ('repeat_type', models.IntegerField(verbose_name='重复方式')),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='monitor.device', verbose_name='设备名称')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='controller.deviceorder', verbose_name='设备指令')),
            ],
            options={
                'verbose_name': '定时控制表',
                'verbose_name_plural': '定时控制表',
            },
        ),
        migrations.CreateModel(
            name='ThresholdControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('threshold', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='阈值')),
                ('indicator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='monitor.environmentindicator', verbose_name='环境指标')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='controller.deviceorder', verbose_name='设备指令')),
            ],
            options={
                'verbose_name': '阈值控制表',
                'verbose_name_plural': '阈值控制表',
            },
        ),
        migrations.CreateModel(
            name='DeviceControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_type', models.IntegerField(verbose_name='控制方式')),
                ('control_id', models.IntegerField(verbose_name='控制信息')),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='monitor.device', verbose_name='设备名称')),
            ],
            options={
                'verbose_name': '设备控制表',
                'verbose_name_plural': '设备控制表',
            },
        ),
        migrations.CreateModel(
            name='ControlHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_type', models.IntegerField(verbose_name='控制方式')),
                ('create_time', models.DateTimeField(verbose_name='操作时间')),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='monitor.device', verbose_name='设备名称')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='controller.deviceorder', verbose_name='设备指令')),
            ],
            options={
                'verbose_name': '设备命令表',
                'verbose_name_plural': '设备命令表',
            },
        ),
        migrations.CreateModel(
            name='BookControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('stop_time', models.DateTimeField(verbose_name='结束时间')),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='monitor.device', verbose_name='设备名称')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='controller.deviceorder', verbose_name='设备指令')),
            ],
            options={
                'verbose_name': '预约控制表',
                'verbose_name_plural': '预约控制表',
            },
        ),
    ]