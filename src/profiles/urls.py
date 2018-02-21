from django.urls import path, re_path, include

from .views import ProfileDetailView

app_name="trydjango1-11"

urlpatterns = [
    re_path(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
]
