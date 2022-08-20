from django.contrib import admin
from car_num.models import PlateNum


class PlateNumAdmin(admin.ModelAdmin):
    list_display = ['num', 'country', 'comment',  'author']
    search_fields = ['num']
    list_per_page = 8

admin.site.register(PlateNum, PlateNumAdmin)