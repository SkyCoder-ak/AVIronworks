# Generated by Django 3.0.5 on 2020-09-10 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0008_auto_20200910_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cooler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cooler_img', models.ImageField(default='', upload_to='images')),
                ('cooler_head', models.CharField(default='', max_length=50)),
                ('cooler_price', models.IntegerField(default=0)),
                ('cooler_height', models.FloatField(default=0)),
                ('cooler_width', models.FloatField(default=0)),
                ('cooler_weight', models.FloatField(default=0)),
                ('cooler_color', models.CharField(default='', max_length=30)),
                ('cooler_inst_facility', models.CharField(default='', max_length=20)),
                ('cooler_accessories', models.CharField(default='', max_length=200)),
                ('cooler_desc', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('door_img', models.ImageField(default='', upload_to='images')),
                ('door_head', models.CharField(default='', max_length=50)),
                ('door_price', models.IntegerField(default=0)),
                ('door_height', models.FloatField(default=0)),
                ('door_width', models.FloatField(default=0)),
                ('door_weight', models.FloatField(default=0)),
                ('door_color', models.CharField(default='', max_length=30)),
                ('door_inst_facility', models.CharField(default='', max_length=20)),
                ('door_accessories', models.CharField(default='', max_length=200)),
                ('door_desc', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FarmingTool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmingtool_img', models.ImageField(default='', upload_to='images')),
                ('farmingtool_head', models.CharField(default='', max_length=50)),
                ('farmingtool_price', models.IntegerField(default=0)),
                ('farmingtool_height', models.FloatField(default=0)),
                ('farmingtool_width', models.FloatField(default=0)),
                ('farmingtool_weight', models.FloatField(default=0)),
                ('farmingtool_color', models.CharField(default='', max_length=30)),
                ('farmingtool_inst_facility', models.CharField(default='', max_length=20)),
                ('farmingtool_accessories', models.CharField(default='', max_length=200)),
                ('farmingtool_desc', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gate_img', models.ImageField(default='', upload_to='images')),
                ('gate_head', models.CharField(default='', max_length=50)),
                ('gate_price', models.IntegerField(default=0)),
                ('gate_height', models.FloatField(default=0)),
                ('gate_width', models.FloatField(default=0)),
                ('gate_weight', models.FloatField(default=0)),
                ('gate_color', models.CharField(default='', max_length=30)),
                ('gate_inst_facility', models.CharField(default='', max_length=20)),
                ('gate_accessories', models.CharField(default='', max_length=200)),
                ('gate_desc', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Grill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grill_img', models.ImageField(default='', upload_to='images')),
                ('grill_head', models.CharField(default='', max_length=50)),
                ('grill_price', models.IntegerField(default=0)),
                ('grill_height', models.FloatField(default=0)),
                ('grill_width', models.FloatField(default=0)),
                ('grill_weight', models.FloatField(default=0)),
                ('grill_color', models.CharField(default='', max_length=30)),
                ('grill_inst_facility', models.CharField(default='', max_length=20)),
                ('grill_accessories', models.CharField(default='', max_length=200)),
                ('grill_desc', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Makhar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('makhar_img', models.ImageField(default='', upload_to='images')),
                ('makhar_head', models.CharField(default='', max_length=50)),
                ('makhar_price', models.IntegerField(default=0)),
                ('makhar_height', models.FloatField(default=0)),
                ('makhar_width', models.FloatField(default=0)),
                ('makhar_weight', models.FloatField(default=0)),
                ('makhar_color', models.CharField(default='', max_length=30)),
                ('makhar_inst_facility', models.CharField(default='', max_length=20)),
                ('makhar_accessories', models.CharField(default='', max_length=200)),
                ('makhar_desc', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Shutter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shutter_img', models.ImageField(default='', upload_to='images')),
                ('shutter_head', models.CharField(default='', max_length=50)),
                ('shutter_price', models.IntegerField(default=0)),
                ('shutter_height', models.FloatField(default=0)),
                ('shutter_width', models.FloatField(default=0)),
                ('shutter_weight', models.FloatField(default=0)),
                ('shutter_color', models.CharField(default='', max_length=30)),
                ('shutter_inst_facility', models.CharField(default='', max_length=20)),
                ('shutter_accessories', models.CharField(default='', max_length=200)),
                ('shutter_desc', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Stair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stair_img', models.ImageField(default='', upload_to='images')),
                ('stair_head', models.CharField(default='', max_length=50)),
                ('stair_price', models.IntegerField(default=0)),
                ('stair_height', models.FloatField(default=0)),
                ('stair_width', models.FloatField(default=0)),
                ('stair_weight', models.FloatField(default=0)),
                ('stair_color', models.CharField(default='', max_length=30)),
                ('stair_inst_facility', models.CharField(default='', max_length=20)),
                ('stair_accessories', models.CharField(default='', max_length=200)),
                ('stair_desc', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TinShed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tinshed_img', models.ImageField(default='', upload_to='images')),
                ('tinshed_head', models.CharField(default='', max_length=50)),
                ('tinshed_price', models.IntegerField(default=0)),
                ('tinshed_height', models.FloatField(default=0)),
                ('tinshed_width', models.FloatField(default=0)),
                ('tinshed_weight', models.FloatField(default=0)),
                ('tinshed_color', models.CharField(default='', max_length=30)),
                ('tinshed_inst_facility', models.CharField(default='', max_length=20)),
                ('tinshed_accessories', models.CharField(default='', max_length=200)),
                ('tinshed_desc', models.CharField(default='', max_length=200)),
            ],
        ),
    ]