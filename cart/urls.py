from django.conf.urls import patterns, url

from cart import views


urlpatterns = patterns('',
    url(r'^add/$',views.add,name = 'add'),
    url(r'^update/$',views.update,name = 'update'),
    url(r'^clear/(?P<cid>\d+)/$',views.clear,name = 'clear'),
    url(r'^delete/$',views.delete,name = 'delete'),
)