from django.conf.urls import url 
from user import views 
 
urlpatterns = [ 
    url(r'^user/$', views.user_list)
]
