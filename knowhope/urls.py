from django.conf.urls import patterns, include, url
from knowhope import appController

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('knowhope',
    # Examples:
    # url(r'^$', 'knowhope.views.home', name='home'),
    # url(r'^knowhope/', include('knowhope.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += appController.urlpatterns