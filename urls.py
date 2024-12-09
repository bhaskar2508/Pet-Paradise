"""
URL configuration for petpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from  .import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home),
    path('register',v.register_view,name='register'),
    path('login',v.login_view,name='login'),
    path('logout',v.logout_view,name='logout'),
    path('store',v.store_view,name='store'),
    path('cat-food',v.cat_food,name='cat-food'),
    path('cat-toys',v.toys,name='cat-toys'),
    path('cat-health',v.cat_health,name='cat-health'),
    path('dog-food',v.dog_food,name='dog-food'),
    path('dog-toys',v.dog_toys,name='dog-toys'),
    path('dog-health',v.dog_health,name='dog-health'),
    path('cart',v.cart_view,name='cart'),
    path('delete1',v.delete,name='delete1'),
    path('delete2',v.delete_cat_health,name='delete2'),
    path('delete3',v.delete_cat_toy,name='delete3'),
    path('delete4',v.delete_dog_food,name='delete4'),
    path('delete5',v.delete_dog_toys,name='delete5'),
    path('delete6',v.delete_dog_health,name='delet5'),
    path('add_to_cart/<int:pid>',v.add_to_cart,name='add_to_cart'),
    path('add_to_cart_01/<int:chid>',v.cat_health_cart,name='add_to_cart_01'),
    path('add_to_cart_02/<int:cit>',v.cat_toy_cart,name='add_to_cart_02'),
    path('add_to_cart_03/<int:dfd>',v.dog_food_cart,name='add_to_cart_03'),
    path('add_to_cart_04/<int:dtd>',v.dog_toys_cart,name='add_to_cart_04'),
    path('add_to_cart_05/<int:dhd>',v.dog_health_cart,name='add_to_cart_05'),
    path('pay_now',v.pay_now_views,name='pay_now'),
]
