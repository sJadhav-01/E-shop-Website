# views under this file are moved to files in views folder




# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib.auth.hashers import make_password, check_password
# from .models.product import Product
# from .models.category import Category 
# from .models.customer import Customer
# from django.views import View

# Create your views here.

# def Index(request): 
#     # return render(request, 'index.html')
#     def Index(request): 
#     # return render(request, 'index.html')
#     return render(request, 'orders/orders.html')

# def index(request):
#     # products = Product.get_all_products()
#     products = None
#     categories = Category.get_all_categories()
#     # print(products)
#     # print(categories)
#     # print(request.GET)   # shows the data sent by get menthod in link '/?category=1'
#     categoryID = request.GET.get('category')
#     if categoryID:
#         products = Product.get_all_products_by_categoryid(categoryID)
#     else:
#         products = Product.get_all_products()
#     data = {}
#     data['products'] = products
#     data['categories'] = categories
#     return render(request, 'index.html', data)


# def validateCustomer(cust_obj):
#     error_message = None

#     if not cust_obj.first_name:
#         error_message = 'First name required !!'
#     elif len(cust_obj.first_name) < 3 :
#         error_message = "First name should be greater than 2 characters"
#     elif not cust_obj.last_name:
#         error_message = 'Last name required !!'
#     elif len(cust_obj.last_name) < 3 :
#         error_message = "Last name should be greater than 2 characters"
#     elif not cust_obj.phone:
#         error_message = 'Phone number required !!'
#     elif len(cust_obj.phone) < 10 :
#         error_message = "Phone number should be 10 characters long"
#     elif not cust_obj.email:
#         error_message = 'Email required !!'
#     elif len(cust_obj.email) < 5 :
#         error_message = "Email should be greater than 5 characters"
#     elif not cust_obj.password:
#         error_message = 'password required !!'
#     elif len(cust_obj.password) < 6 :
#         error_message = "Password should be greater than 6 characters"
#     elif cust_obj.IsEmailExists():
#         error_message = "Email address is already registered !!"

#     return error_message


# def registerCustomer(request):  # this will handle if the request is post request

#     post_data = request.POST
#     fn = post_data.get('first_name')
#     ln = post_data.get('last_name')
#     ph = post_data.get('phone')
#     em = post_data.get('email')
#     pw = post_data.get('password')

#     # validation
#     values = {
#         'fn' : fn,
#         'ln' : ln,
#         'ph' : ph,
#         'em' : em
#     }    # storing these values in dictionary and sending them to html page to show the values entered when the error occured due to one of the value entered
    
#     customer = Customer(first_name = fn, last_name = ln, phone = ph, email = em, password = pw) 

#     error_message = validateCustomer(customer)

#     # saving
#     if not error_message:
#         customer.password = make_password(customer.password)  # hashed the entered password by user before saving into database
#         customer.register()  # customer.save() can be used instead of register methode created in customer.py file 
#         return redirect('homepage')
#     else:
#         data = {
#             'error' : error_message,
#             'values' : values
#         }
#         return render(request, 'signup.html', data)


# def signup(request):   
#     if request.method == 'GET': 
#         return render(request, 'signup.html')
#     else:
#         return registerCustomer(request)
       

        # seperating signup code in different chuncks for better readability and to easy management - createing validation function and userregistration method seperately above the signup method.


# def Login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html') 
#     else:  
#         cust_email = request.POST.get('email')
#         cust_pass = request.POST.get('password')
#         customer = Customer.getCustomerByEmail(cust_email)
#         print(customer.email, customer.password, customer.first_name)
#         error_message = None
#         if customer:
#             flag = check_password(cust_pass, customer.password)
#             if flag:
#                 return redirect('homepage')
#             else:
#                 error_message = 'Email or password is invalid !!'  
#         else:
#             error_message = 'Email or password is invalid !!'
#         return render(request, 'login.html', {'error' : error_message}) 





