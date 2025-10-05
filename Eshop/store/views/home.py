from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category 
from django.views import View



class Index(View):   

    def get(self, request):
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        return render(request, 'index.html', data)
    

    def post(self, request):
        product = request.POST.get('product')  # we receive product id here by the product parameter
        remove = request.POST.get('remove')
        # print(product)
        # managing cart
        cart = request.session.get('cart')  # check if dictionary named cart is present in sessions, if not create one.
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:                    
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else: 
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart  # assigning or adding cart dictionary to session
        print('customer', request.session.get('customer_id'))
        print('customer', request.session.get('customer_email'))
        print('cart', request.session['cart'])    

        return redirect('homepage')


    