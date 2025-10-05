from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product

class Cart(View):

    def get(self, request):
        cart = request.session.get('cart')
        cart_product = {}
        if not cart:
            return render(request, 'cart.html')  # Handle empty cart case
        
        for product_id in cart:
            product = Product.get_product_by_id(product_id)
            # print(product.name)
            # print(cart[product_id])
            cart_product[product_id] = (product, cart[product_id])
        # print(cart)
        # print(cart_product)
        return render(request, 'cart.html', {'cart': cart_product}) 