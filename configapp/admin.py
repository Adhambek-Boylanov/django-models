from django.contrib import admin
from .models import *

class ViloyatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ['title']
    search_fields = ['title']

class TumanAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','created_ed','update_ed','viloyat')
    list_display_links = ['title','update_ed','viloyat']
    search_fields = ['title']

class MahallaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','created_ed','update_ed','tuman')
    list_display_links = ['title','update_ed','tuman']
    search_fields = ['title']

admin.site.register(Viloyat,ViloyatAdmin)
admin.site.register(Tuman,TumanAdmin)
admin.site.register(Mahalla,MahallaAdmin)

# admin.site.register([Viloyat,Tuman,Mahalla])
