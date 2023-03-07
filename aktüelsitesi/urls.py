from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path("<category_name>", views.listbycategoryname),
]