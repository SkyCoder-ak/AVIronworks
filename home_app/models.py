from django.db import models

# Create your models here.
class SliderData(models.Model):
    slider_head = models.CharField(max_length=50,default='')
    slider_desc = models.CharField(max_length=200,default='')
    slider_img = models.ImageField(upload_to='images',default='')

CATEGORIES = (
    ('gates_and_doors','Gates and Doors'),
    ('grills','Grills'),
    ('tin_sheds','Tin Sheds'),
    ('farming_tools','Farming Tools'),
    ('air_coolers','Air Coolers'),
    ('gauri_makhars','Gauri Makhars'),
    ('stairs','Stairs'),
    ('shutters','Shutters'),
    ('others','Others'),
)

class Products(models.Model):
    prod_cat = models.CharField(max_length=30,choices=CATEGORIES,default='')
    prod_head = models.CharField(max_length=50,default='')
    prod_price = models.IntegerField(default=0)
    prod_height = models.FloatField(default=0)
    prod_width = models.FloatField(default=0)
    prod_weight = models.FloatField(default=0)
    prod_color = models.CharField(max_length=30,default='')
    prod_inst_facility = models.CharField(max_length=20,default='')
    prod_accessories = models.CharField(max_length=200,default='')
    prod_desc = models.CharField(max_length=200,default='')
    prod_img = models.ImageField(upload_to='images',default='')

    

# class Gate(models.Model):
#     gate_img = models.ImageField(upload_to='images',default='')
#     gate_head = models.CharField(max_length=50,default='')
#     gate_price = models.IntegerField(default=0)
#     gate_height = models.FloatField(default=0)
#     gate_width = models.FloatField(default=0)
#     gate_weight = models.FloatField(default=0)
#     gate_color = models.CharField(max_length=30,default='')
#     gate_inst_facility = models.CharField(max_length=20,default='')
#     gate_accessories = models.CharField(max_length=200,default='')
#     gate_desc = models.CharField(max_length=200,default='')

# class Grill(models.Model):
#     grill_img = models.ImageField(upload_to='images',default='')
#     grill_head = models.CharField(max_length=50,default='')
#     grill_price = models.IntegerField(default=0)
#     grill_height = models.FloatField(default=0)
#     grill_width = models.FloatField(default=0)
#     grill_weight = models.FloatField(default=0)
#     grill_color = models.CharField(max_length=30,default='')
#     grill_inst_facility = models.CharField(max_length=20,default='')
#     grill_accessories = models.CharField(max_length=200,default='')
#     grill_desc = models.CharField(max_length=200,default='')

# class Door(models.Model):
#     door_img = models.ImageField(upload_to='images',default='')
#     door_head = models.CharField(max_length=50,default='')
#     door_price = models.IntegerField(default=0)
#     door_height = models.FloatField(default=0)
#     door_width = models.FloatField(default=0)
#     door_weight = models.FloatField(default=0)
#     door_color = models.CharField(max_length=30,default='')
#     door_inst_facility = models.CharField(max_length=20,default='')
#     door_accessories = models.CharField(max_length=200,default='')
#     door_desc = models.CharField(max_length=200,default='')

# class TinShed(models.Model):
#     tinshed_img = models.ImageField(upload_to='images',default='')
#     tinshed_head = models.CharField(max_length=50,default='')
#     tinshed_price = models.IntegerField(default=0)
#     tinshed_height = models.FloatField(default=0)
#     tinshed_width = models.FloatField(default=0)
#     tinshed_weight = models.FloatField(default=0)
#     tinshed_color = models.CharField(max_length=30,default='')
#     tinshed_inst_facility = models.CharField(max_length=20,default='')
#     tinshed_accessories = models.CharField(max_length=200,default='')
#     tinshed_desc = models.CharField(max_length=200,default='')

# class FarmingTool(models.Model):
#     farmingtool_img = models.ImageField(upload_to='images',default='')
#     farmingtool_head = models.CharField(max_length=50,default='')
#     farmingtool_price = models.IntegerField(default=0)
#     farmingtool_height = models.FloatField(default=0)
#     farmingtool_width = models.FloatField(default=0)
#     farmingtool_weight = models.FloatField(default=0)
#     farmingtool_color = models.CharField(max_length=30,default='')
#     farmingtool_inst_facility = models.CharField(max_length=20,default='')
#     farmingtool_accessories = models.CharField(max_length=200,default='')
#     farmingtool_desc = models.CharField(max_length=200,default='')

# class Cooler(models.Model):
#     cooler_img = models.ImageField(upload_to='images',default='')
#     cooler_head = models.CharField(max_length=50,default='')
#     cooler_price = models.IntegerField(default=0)
#     cooler_height = models.FloatField(default=0)
#     cooler_width = models.FloatField(default=0)
#     cooler_weight = models.FloatField(default=0)
#     cooler_color = models.CharField(max_length=30,default='')
#     cooler_inst_facility = models.CharField(max_length=20,default='')
#     cooler_accessories = models.CharField(max_length=200,default='')
#     cooler_desc = models.CharField(max_length=200,default='')

# class Makhar(models.Model):
#     makhar_img = models.ImageField(upload_to='images',default='')
#     makhar_head = models.CharField(max_length=50,default='')
#     makhar_price = models.IntegerField(default=0)
#     makhar_height = models.FloatField(default=0)
#     makhar_width = models.FloatField(default=0)
#     makhar_weight = models.FloatField(default=0)
#     makhar_color = models.CharField(max_length=30,default='')
#     makhar_inst_facility = models.CharField(max_length=20,default='')
#     makhar_accessories = models.CharField(max_length=200,default='')
#     makhar_desc = models.CharField(max_length=200,default='')

# class Stair(models.Model):
#     stair_img = models.ImageField(upload_to='images',default='')
#     stair_head = models.CharField(max_length=50,default='')
#     stair_price = models.IntegerField(default=0)
#     stair_height = models.FloatField(default=0)
#     stair_width = models.FloatField(default=0)
#     stair_weight = models.FloatField(default=0)
#     stair_color = models.CharField(max_length=30,default='')
#     stair_inst_facility = models.CharField(max_length=20,default='')
#     stair_accessories = models.CharField(max_length=200,default='')
#     stair_desc = models.CharField(max_length=200,default='')

# class Shutter(models.Model):
#     shutter_img = models.ImageField(upload_to='images',default='')
#     shutter_head = models.CharField(max_length=50,default='')
#     shutter_price = models.IntegerField(default=0)
#     shutter_height = models.FloatField(default=0)
#     shutter_width = models.FloatField(default=0)
#     shutter_weight = models.FloatField(default=0)
#     shutter_color = models.CharField(max_length=30,default='')
#     shutter_inst_facility = models.CharField(max_length=20,default='')
#     shutter_accessories = models.CharField(max_length=200,default='')
#     shutter_desc = models.CharField(max_length=200,default='')