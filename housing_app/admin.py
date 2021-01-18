from django.contrib import admin

from .models import neighborhood_data, housing_data

admin.site.register(neighborhood_data)
admin.site.register(housing_data)