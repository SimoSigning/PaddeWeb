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
    url(r'^profil/$', PaddeApp.views.profil, name='profil'),
    url(r'^view_profile', PaddeApp.views.view_profile, name='view_profile'),
    url(r'^login/$', PaddeApp.views.login, name='login'),
    url(r'^auth/$',PaddeApp.views.auth_view, name='auth_view'),
    url(r'^logout/$',PaddeApp.views.logout, name='logout'),
    url(r'^loggedin/$', PaddeApp.views.loggedin, name='loggedin'),
    url(r'^invalid/$', PaddeApp.views.invalid_login, name='invalid'),
    url(r'^register/$', PaddeApp.views.register_user, name ='register'),
    url(r'^register_success/$', PaddeApp.views.register_success, name='register_success'),
    url(r'^create_fav_turtle/$', PaddeApp.views.create_fav_turtle, name='create_fav_turtle'),
    # Examples:
    # url(r'^$', PaddeWeb.views.home, name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls))
]
