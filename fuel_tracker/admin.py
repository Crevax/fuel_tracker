from django.contrib import admin
from fuel_tracker.models import *

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('owner', 'nickname', 'make', 'model', 'year')

class GasCompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)

class GasStationAdmin(admin.ModelAdmin):
    list_display = ('company', 'street_address', 'city', 'state', 'zipcode')

class FuelUpAdmin(admin.ModelAdmin):
    list_display = ('date', 'vehicle', 'station', 'cost', 'mpg')
    date_hierarchy = 'date'

    def cost(self, obj):
        return '$%.2f' % obj.cost

    def mpg(self, obj):
        if obj.mpg == 'N/A':
            return 'N/A'
        else:
            return '%.2f' % obj.mpg

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'website')

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(GasCompany, GasCompanyAdmin)
admin.site.register(GasStation, GasStationAdmin)
admin.site.register(FuelUp, FuelUpAdmin)
admin.site.register(UserProfile, UserProfileAdmin)