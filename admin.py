from django.contrib import admin
from .models import uporabnik
from django.contrib.auth.models import Group



# Register your models here.


class UporabnikAdmin(admin.ModelAdmin):
    list_display = ('mail','datum_vpisa','emso')
    list_filter = ('datum_vpisa', 'emso')
    search_fields = ('emso','mail')


admin.site.site_header = 'Nadzorniški pregled'


admin.site.register(uporabnik, UporabnikAdmin)
admin.site.unregister(Group)

