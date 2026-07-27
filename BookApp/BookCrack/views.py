from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def product(request):
    return render(request, 'products.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def checkoutadv1(request):
    return render(request, 'checkoutadv1.html')

def checkoutadv2(request):
    return render(request, 'checkoutadv2.html')

def checkoutk1(request):
    return render(request, 'checkoutk1.html')

def checkoutk2(request):
    return render(request, 'checkoutk2.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        # Add success message to Django Messages framework
        messages.success(request, 'Account created successfully!')
        # Redirect directly to home (index.html)
        return redirect('/')
        
    return render(request, 'signup.html')

def product_detail(request):
    return render(request, 'products.html')

def advdetails(request):
    return render(request, 'advdetails.html')

def kiddetails(request):
    return render(request, 'kiddetails.html')   

def fandetails(request):
    return render(request, 'fandetails.html')   

def edudetails(request):
    return render(request, 'edudetails.html')   

def scidetails(request):
    return render(request, 'scidetails.html')

def interest(request):
    return render(request, 'interest.html')