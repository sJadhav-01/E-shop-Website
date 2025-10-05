from django.shortcuts import redirect
from django.views import View
from store.models.product import Product
from store.models.order import Order
from store.models.customer import Customer

class CheckOut(View):
    def get(self, request):
        if request.session.get('customer'):
            return redirect('cart')
        else:
            return redirect('login')


    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get("phone")
        customer_id = request.session.get('customer')
        if customer_id:
            cart = request.session.get('cart')

            for product_id, quantity in cart.items():
                product = Product.get_product_by_id(product_id)
                customer = Customer.objects.get(id=customer_id)
                order = Order(customer= customer, product= product, quantity= quantity, price= product.price, phone= phone, address= address)
                order.place_order()

                request.session['cart'] = {}
        else:
            return redirect('login')
        return redirect('orders') 


