from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^userlist/', views.get_list),
    url(r'^profile/', views.profile),
    url(r'^physiological/', views.physiological),
]
