"""
Definition of urls for PaddeWeb.
"""

from django.conf.urls import include, url
import PaddeApp.views
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', PaddeApp.views.index, name='index'),
    url(r'^home$', PaddeApp.views.index, name='home'),
    url(r'^udbredelse$', PaddeApp.views.udbredelse, name='udbredelse'),
    url(r'^skjoldet$', PaddeApp.views.skjoldet, name='skjoldet'),
    url(r'^sanser$', PaddeApp.views.sanser, name='sanser'),
    url(r'^om$', PaddeApp.views.om, name='om'),
    url(r'^register/$', PaddeApp.views.register, name='register'),
    url(r'^profil$', PaddeApp.views.profil, name='profil'),
    url(r'^login/$', login, {'template_name':'PaddeApp/login.html'}),
    url(r'^logout/$', logout, {'template_name':'PaddeApp/logout.html'}),   
    # Examples:
    # url(r'^$', PaddeWeb.views.home, name='home'),
    # url(r'^PaddeWeb/', include('PaddeWeb.PaddeWeb.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls))
]
