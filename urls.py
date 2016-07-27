
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home_page,name='home'),
    url(r'^home/$',views.home_page,name='home'),
    url(r'^Business/$',views.business_page,name='Business'),
    
    
    url(r'^Client/$',views.client_page,name='Client'),
    

    
    url(r'^add-content/$',views.user_profile,name='user_profile'),
    url(r'^user/$',views.logedin,name='Client'),

    url(r'^profile/$',views.user_profile,name='user_profile'),

    url(r'^Client/5/$',views.biz_item,name='biz_items'),
    
    
    
    
    
]
