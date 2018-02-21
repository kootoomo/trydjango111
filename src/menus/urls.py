from django.urls import path
from django.urls import include, re_path

from .views import (
	ItemCreateView,
	ItemDetailView,
	ItemListView,
	ItemUpdateView,	
)

app_name="trydjango1-11"

urlpatterns = [ 
    re_path(r'^create/$', ItemCreateView.as_view(), name='create'),
    #re_path(r'^(?P<pk>\d+)/edit$', ItemUpdateView.as_view(), name='edit'),
    re_path(r'^(?P<pk>\d+)/$', ItemUpdateView.as_view(), name='detail'),
    re_path(r'^$', ItemListView.as_view(), name='list'),
    ]