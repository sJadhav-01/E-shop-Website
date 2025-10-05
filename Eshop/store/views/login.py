from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import View


class Login(View):
    return_url = None
    def get(self, request):
        print('get_method')
        Login.return_url = request.GET.get('return_url')
        print(Login.return_url)
        return render(request, 'login.html')
    
    def post(self, request):
        cust_email = request.POST.get('email')
        cust_pass = request.POST.get('password')
        customer = Customer.getCustomerByEmail(cust_email)
        # print(customer.email, customer.password, customer.first_name)
        error_message = None
        if customer:
            flag = check_password(cust_pass, customer.password)
            if flag:
                request.session['customer'] = customer.id  # we will use this to handle login/logout/signup link dynamically
                request.session['customer_name'] = customer.first_name
                request.session['customer_email'] = customer.email
                print('customer', request.session.get('customer_email'))
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Email or password is invalid !!'  
        else:
            error_message = 'Email or password is invalid !!'
        return render(request, 'login.html', {'error' : error_message}) 
