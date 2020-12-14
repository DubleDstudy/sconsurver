from django.conf.urls import url
from comment1 import views

urlpatterns = [

    url(r'^comment1/$', views.comment1_list),
]

