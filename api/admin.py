from django.contrib import admin

from rest_framework.authtoken.admin import TokenAdmin

from .models import Train, Schedule, Line, Driver, Station

# Register your models here.
admin.site.register(Train)
admin.site.register(Schedule)
admin.site.register(Line)
admin.site.register(Driver)
admin.site.register(Station)

TokenAdmin.raw_id_fields = ('user',)
