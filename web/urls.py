from django.conf.urls import url
from . import views

app_name = 'info'

urlpatterns = [
    url(r'^$', views.InfoIndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.InfoDetailView.as_view(), name='detail'),
]