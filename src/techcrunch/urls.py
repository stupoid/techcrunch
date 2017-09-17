from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login', auth_views.login, {'template_name': 'techcrunch/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^map/$', views.map, name='map'),
    url(r'^shelter_routing/$', views.shelter_routing, name='shelter_routing'),
    url(r'^', views.index, name='index'),
]
