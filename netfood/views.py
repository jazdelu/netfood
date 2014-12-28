from django.shortcuts import render_to_response
from django.http import Http404
from django.template import RequestContext
from menu.models import MenuItem, Category

def home(request):
	items = MenuItem.objects.filter(recommend = True)
	categories = Category.objects.all()
	items_rank = MenuItem.objects.all().order_by("-sold")[:5]
	return render_to_response("index.html",{ "items":items,"categories":categories,"items_rank":items_rank },context_instance = RequestContext(request))
