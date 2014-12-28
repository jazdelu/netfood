from django.conf.urls import patterns, url

from order import views


urlpatterns = patterns('',
	url(r'^$',views.get_orders,name = 'get orders'),
    url(r'^check/$',views.check,name = 'check'),
    url(r'^submit/$',views.submit,name = 'submit'),
    url(r'^change_status/$',views.change_status,name = 'change status')
)