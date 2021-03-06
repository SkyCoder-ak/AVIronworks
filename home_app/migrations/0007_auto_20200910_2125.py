# Generated by Django 3.0.5 on 2020-09-10 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0006_auto_20200910_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='prod_accessories',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='products',
            name='prod_color',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='products',
            name='prod_desc',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='products',
            name='prod_height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='prod_inst_facility',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='products',
            name='prod_weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='prod_width',
            field=models.IntegerField(default=0),
        ),
    ]
