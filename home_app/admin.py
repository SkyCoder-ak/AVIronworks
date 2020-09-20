from django.contrib import admin
from home_app.models import SliderData
from home_app.models import Products

# Register your models here.
class SliderDataAdmin(admin.ModelAdmin):
    list_display = ['slider_head','slider_desc','slider_img']

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['prod_cat','prod_head','prod_price','prod_height','prod_width','prod_weight','prod_color','prod_inst_facility','prod_accessories','prod_desc','prod_img']

admin.site.register(SliderData,SliderDataAdmin)
admin.site.register(Products,ProductsAdmin)