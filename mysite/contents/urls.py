from django.conf.urls import url 
from contents import views 
 
urlpatterns = [ 
    url(r'^contents/$', views.contents_list),
]
