"""
Definition of urls for ServicioDaon1_1.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', ServicioDaon1_1.views.home, name='home'),
    # url(r'^ServicioDaon1_1/', include('ServicioDaon1_1.ServicioDaon1_1.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     #url('admin/', admin.site.urls),
     url('api/',include('bosques.urls')),
]
