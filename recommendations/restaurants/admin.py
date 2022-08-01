from django.contrib import admin

from .models import Restaurant, Neighborhood, Borough

admin.site.register(Restaurant)
admin.site.register(Neighborhood)
admin.site.register(Borough)