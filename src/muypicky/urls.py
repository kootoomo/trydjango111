from django.contrib import admin
from django.urls import path, include
from django.urls import re_path

from django.views.generic import TemplateView

from django.contrib.auth.views import LoginView, LogoutView

from menus.views import HomeView
from profiles.views import ProfileFollowToggle, RegisterView, activate_user_view

app_name="trydjango1-11"

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', HomeView.as_view(), name='home'),
    re_path(r'^register/$', RegisterView.as_view(), name='register'),
    re_path(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^profile-follow/$', ProfileFollowToggle.as_view(), name='follow'),
    path('u/', include('profiles.urls', namespace='profiles')),
    path('items/', include('menus.urls', namespace='menus')),
    path('restaurants/', include('restaurants.urls', namespace='restaurants')),
    re_path(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    re_path(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact')
    ]
    