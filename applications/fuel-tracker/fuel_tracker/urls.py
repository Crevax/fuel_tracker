from django.conf.urls import patterns, url
from fuel_tracker.views import main, vehicle, gas_company, gas_station, fuel_up

# Main URLs 
urlpatterns = patterns('main',
    url(r'^$', main.index, name='main.index'),
    url(r'^register/$', main.register, name='main.register'),
    url(r'^login/$', main.user_login, name='main.login'),
    url(r'^logout/$', main.user_logout, name='main.logout'),        
)
# Vehicle URLs
urlpatterns += patterns('',
    url(r'^vehicle/$', vehicle.index, name='vehicle.index'),
    url(r'^vehicle/add/$', vehicle.add, name='vehicle.add'),   
    url(r'^vehicle/(?P<owner_name>\w+)/(?P<vehicle_nickname>\w+)/$', vehicle.detail, name='vehicle.detail'),
    url(r'^vehicle/(?P<owner_name>\w+)/(?P<vehicle_nickname>\w+)/edit/$', vehicle.edit, name='vehicle.edit'), 
)
# Gas Company URLs
urlpatterns += patterns('',
    url(r'^gas_company/$', gas_company.index, name='gas_company.index'),
    url(r'^gas_company/add/$', gas_company.add, name='gas_company.add'),    
)
# Gas Station URLs
urlpatterns += patterns('',
    url(r'^gas_station/$', gas_station.index, name='gas_station.index'),    
    url(r'^gas_station/add/$', gas_station.add, name='gas_station.add'),
)
# Fuel Up URLs
urlpatterns += patterns('',
    url(r'^fuel_up/$', fuel_up.index, name='fuel_up.index'),
    url(r'^fuel_up/add/$', fuel_up.add, name='fuel_up.add'),
)