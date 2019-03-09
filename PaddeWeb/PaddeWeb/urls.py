"""
Definition of urls for PaddeWeb.
"""

from django.conf.urls import include, url
import PaddeApp.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', PaddeApp.views.index, name='index'),
    url(r'^home$', PaddeApp.views.index, name='home'),
    # Examples:
    # url(r'^$', PaddeWeb.views.home, name='home'),
    # url(r'^PaddeWeb/', include('PaddeWeb.PaddeWeb.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
