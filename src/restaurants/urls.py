from django.urls import path
from django.urls import include, re_path

from .views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView,
    RestaurantUpdateView
)

app_name="trydjango1-11"

urlpatterns = [ 
    re_path(r'^create/$', RestaurantCreateView.as_view(), name='create'),
	#re_path(r'^(?P<slug>[\w-]+)/edit/$', RestaurantUpdateView.as_view(), name='edit'),
	re_path(r'^(?P<slug>[\w-]+)/$', RestaurantUpdateView.as_view(), name='detail'),
    re_path(r'^$', RestaurantListView.as_view(), name='list'),
    ]