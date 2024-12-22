from django.urls import path
from . import views
# from web.web.urls import urlpatterns


urlpatterns = [
    path('', views.index),
    path('new', views.new)
]