from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('event', views.event, name='event'),
]




urlpatterns += [
    # url(r'^event/create/(?P<pk>\d+)$', views.EventCreate.as_view(), name='event_create'),
    # path('event/create/', views.EventCreate.as_view(), name='event_create'),
    url(r'^event/create/$', views.EventCreate.as_view(), name='event_create'),
    url(r'^event/(?P<pk>\d+)/update/$', views.EventUpdate.as_view(), name='event_update'),
    url(r'^event/(?P<pk>\d+)/delete/$', views.EventDelete.as_view(), name='event_delete'),
    url(r'^event/(?P<pk>\d+)/done/$', views.event_done, name='event_done'),
    url(r'^event/(?P<pk>\d+)/undone/$', views.event_undone, name='event_undone'),

]
