"""
URL configuration for BookApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BookCrack import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('product/',views.product, name='product'),
    path('cart/',views.cart, name='cart'),
    path('checkout/',views.checkout, name='checkout'),
    path('login/',views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('checkoutadv1/',views.checkoutadv1, name='checkoutadv1'),
    path('checkoutadv2/',views.checkoutadv2, name='checkoutadv2'),
    path('checkoutk1/',views.checkoutk1, name='checkoutk1'),
    path('checkoutk2/',views.checkoutk2, name='checkoutk2'),
    path('product_detail/',views.product_detail, name='product_detail'),
    path('kiddetails/',views.kiddetails, name='kiddetails'),
    path('advdetails/',views.advdetails, name='advdetails'),
    path('fandetails/',views.fandetails, name='fandetails'),
    path('edudetails/',views.edudetails, name='edudetails'),
    path('scidetails/',views.scidetails, name='scidetails'),
    path('interest/',views.interest, name='interest'),
]
 