from __future__ import print_function
from cms.sitemaps import CMSSitemap
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from login.views import *
import login.views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^', include('cms.urls')),

)



# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^login/$', 'django.contrib.auth.views.login',name='login'),
        url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
        url(r'^logout/$', logout_page),
        url(r'^dashboard/$', 'login.views.dashbord', name='dashbord'),
        url(r'^send-success/$','login.views.success',name="success_pass"),
        #Registration new user
        url(r'^new-user/$', register),
        url(r'^success/$', register_success ,name="success"),
        #reset Password
        url(r'^update-password/$', 'login.views.reset', name='reset'),
        url(r'^password/reset/confirm/complete/$',login.views.password_reset_complete,name='password_reset_complete'),
         # must be named for reverse to work
        url(r'reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$','login.views.reset_confirm',
            name='password_reset_confirm'),
        url(r'^completed/$', 'login.views.password_reset_completed', name='password_reset_completed'),
        url(r'^profile/$','login.views.profile',name="profile"),
        ) + staticfiles_urlpatterns() + urlpatterns  # NOQA
