from django import template

register = template.Library()

@register.filter(name='is_in_cart')  # this filter is used to check if the product is present in cart or not
def is_in_cart(product, cart):
    if cart:
        keys = cart.keys()
        for id in keys:
            if int(id) == product.id:  # id(key of dict) is a string so converted into int
                return True
    return False

# @register.filter(name='non_zero_product')  # this filter is used to check if the number of product zero
# def non_zero_product (product, cart):
#     q = cart[product]
#     if q != 0:
#         return True
#     return False
    

@register.filter(name='product_quantity_in_cart')
def product_quantity_in_cart(product, cart):
    if cart:
        keys = cart.keys()
        for id in keys:
            if int(id) == product.id:
                return cart.get(id)
    return 0

@register.filter(name='total_calculator')
def total_calculator(product_price, quantity):
    return product_price * quantity


@register.filter(name='final_total')
def final_total(cart):
    total = 0
    for product, quantity in cart.values():
        total += total_calculator(product.price, quantity)
    return total

@register.filter(name='currency')
def currency(number):
    return "₹ "+str(number)