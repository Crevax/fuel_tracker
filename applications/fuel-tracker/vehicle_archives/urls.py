from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vehicle_archives.views.home', name='home'),
    # url(r'^vehicle_archives/', include('vehicle_archives.foo.urls')),

    url(r'^fuel_tracker/', include('fuel_tracker.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
            'serve',
                {'document_root': settings.MEDIA_ROOT}
        ),
    )