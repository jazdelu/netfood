from cart.models import Cart

def get_cart_by_session(request):
	cart =''
	if 'admin' not in request.get_full_path().split('/'):

		if request.session.get('cart'):
			cart = Cart.objects.get(id = request.session.get("cart"))
		else:
			cart = Cart()
			cart.session = '1024'
			cart.save()
			request.session['cart'] = cart.id
	else:
		pass

	return {'cart':cart}
