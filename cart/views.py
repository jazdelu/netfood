from django.shortcuts import render_to_response
from cart.models import Cart, CartItem
from menu.models import *
from django.http import HttpResponse, HttpResponseRedirect
import json
from django.http import Http404
from django.template import RequestContext
# Create your views here.


def add(request):
	cart = ''
	menuitem = ''
	try:
		cart = Cart.objects.get(id = request.session.get("cart"))
		menuitem = MenuItem.objects.get(id = int(request.GET['iid']))
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))

	item = CartItem()
	item.menuitem = menuitem
	item.cart = cart
	item.quantity = 1
	item.price = menuitem.price*item.quantity
	status = 0

	for i in CartItem.objects.filter(cart = cart).filter(menuitem = menuitem):
		if i.menuitem == item.menuitem:
			i.quantity+=item.quantity
			i.price = i.menuitem.price * i.quantity
			i.save()
			item = i 
			status = 1
			break;
	else:
		item.save()
		status = 0
	data = {}
	data['status'] = status
	data['id'] = item.id
	data['name'] = item.menuitem.name
	data['quantity'] = item.quantity
	data['price'] = item.price
	data['total'] = cart.total()
	data['count'] = cart.count()

	return HttpResponse(json.dumps(data),content_type="application/json")

def clear(request,cid):
	cart = ''
	try:
		cart = Cart.objects.get(id = request.session.get("cart"))
	except:
		raise Http404

	for i in cart.items.all():
		i.delete()
	return HttpResponseRedirect("/")

def delete(request):
	item = ''
	cart = ''
	try:
		item = CartItem.objects.get(id = int(request.GET['id']))
		cart = Cart.objects.get(id = request.session.get("cart"))
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))

	data = {}
	data['id'] = item.id
	item.delete()
	data['total'] = cart.total()
	data['count'] = cart.count()
	return HttpResponse(json.dumps(data),content_type="application/json")


def update(request):
	item = ''
	cart = ''
	try:
		item = CartItem.objects.get(id = int(request.GET['id']))
		cart = Cart.objects.get(id = request.session.get("cart"))
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))
	item.quantity = int(request.GET['quantity'])
	item.price = item.menuitem.price*item.quantity
	item.save()
	data = {}
	data['id'] = item.id
	data['price'] = item.price
	data['total'] = cart.total()
	return HttpResponse(json.dumps(data),content_type="application/json")





