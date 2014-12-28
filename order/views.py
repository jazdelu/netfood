from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.http import Http404
from django.template import RequestContext
from django.db.models import Q
import datetime,random
from order.models import Order
from banner.models import Banner
from order.forms import OrderForm
from cart.models import Cart


# Create your views here.
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def check(request):
	ip = get_client_ip(request)
	seat = ip.split('.')[-1]
	banners = Banner.objects.all()[:2]	
	return render_to_response("check.html",{ 'seat':seat,'banners':banners },context_instance=RequestContext(request))


def serial_generator():
	serial ='NF'
	serial+= datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	serial+= str(random.randint(100,999))
	return serial

def submit(request):
	if request.POST:
		form = OrderForm(request.POST)
		if form.is_valid():
			order = form.save(commit = False)
			order.serial = serial_generator()
			order.status = "new"
			order.save()
		else:
			return render_to_response("check.html",{"form":form},context_instance=RequestContext(request))
		try:
			cart = Cart.objects.get(id = request.session.get("cart"))
		except:
			return HttpResponse("Server Error")
		cart.status = 'off'
		cart.save()
		order.cart = cart
		del request.session['cart']

		return HttpResponseRedirect('/')
	else:
		form = OrderForm()
		return HttpResponse("Server Error")


def get_orders(request):
	if request.user.is_authenticated():
		d = datetime.datetime.today()
		d1 = datetime.datetime(d.year,d.month,d.day,0,0,0,0)
		orders = Order.objects.filter(creation_date__gt = d1)
		return render_to_response("order.html",{ "orders":orders },context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/admin/')


def change_status(request):
	status = request.GET['s']
	try:
		order = Order.objects.get(id = int(request.GET['id']))
	except:
		return HttpResponse("Server Error")
	order.status = status
	if status == 'paid':
		for i in order.cart.items.all():
			i.menuitem.sold += i.quantity
			i.menuitem.save()
	order.save()
	return HttpResponse()