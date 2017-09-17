from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login', auth_views.login, {'template_name': 'techcrunch/login.html'}, name='login'),
    url(r'^logout', auth_views.logout, name='logout'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^dashboard/nearby_shelters', views.nearby_shelters, name='nearby_shelters'),
    url(r'^dashboard/residents', views.residents, name='residents'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^create-shelter', views.create_shelter, name='create_shelter'),
    url(r'^map/$', views.map, name='map'),
    url(r'^shelter_routing/$', views.shelter_routing, name='shelter_routing'),
    url(r'^', views.index, name='index'),
]
