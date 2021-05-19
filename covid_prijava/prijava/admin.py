
from django.contrib import admin
from .models import Prijava



# Register your models here.

class UporabnikAdmin(admin.ModelAdmin):
    list_display = ('emso','ime','priimek', 'datum_vpisa')
    list_filter = ('datum_vpisa', 'emso')
    search_fields = ('emso','mail')


admin.site.site_header = 'Nadzorniški pregled'


admin.site.register(Prijava, UporabnikAdmin)
