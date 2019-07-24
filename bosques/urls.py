from django.conf.urls import include, url
from .views import BosquesDetail, ArbolListView, ArbolDetail, BosqueListView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Bosque API')

urlpatterns = [
    url(r'^bosques/(?P<pk>[\w-]+)/$', BosquesDetail.as_view()),
    url(r'^bosques/$', BosqueListView.as_view()),
    url(r'^$', schema_view),
    url(r'^arboles/$', ArbolListView.as_view()),
    url(r'^arboles/(?P<pk>[\w-]+)/$', ArbolDetail.as_view()),

]
