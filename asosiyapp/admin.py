from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *
# Register your models here.

@admin.register(Mahsulot)
class MahsulotModelAdmin(ModelAdmin):
    list_display = ["id", "nom", "brend", "miqdor", "narx", "olchov", "kelgan_sana"]
    search_fields = ['id', 'nom', 'brend',]
    list_filter = ['miqdor',]
    list_editable = ['narx',]
    list_display_links = ['id', 'nom']
admin.site.register(Mijoz)