from django.shortcuts import render, redirect
from django.views import View
from store.models.order import Order
# from store.middlewares.auth import auth_middleware
# from django.utils.decorators import method_decorator # to use middleware before method

class Orders(View):

    # @method_decorator(auth_middleware)  # calling middleware through method decorator
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)

        return render(request, 'orders.html', {'orders': orders})