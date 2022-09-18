from audioop import add
import email
from itertools import product
from math import ceil
from sre_constants import CATEGORY
from unicodedata import category
from django.shortcuts import redirect, render
from django.views import View
from .models import Bloger, Blog
# from math import ceil
from django.http import HttpResponse
from .forms import CustomerRegistrationForm, BlogerProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# def home(request):
#     products = Product.objects.all()
#     print(products)
#     n = len(products)
#     nSlides = n//4 + ceil((n/4)-(n//4))
#     params = {'product': products}
#     return render(request, 'app/home.html', params)

class BlogView(View):
 def get(self, request):
    computer_science = Blog.objects.filter(category='CS')
    social_media = Blog.objects.filter(category='SC')
    politics = Blog.objects.filter(category='PL')
    all = Blog.objects.filter(category='AL')
    return render(request, 'app/home.html',{'computer_science':computer_science, 'social_media': social_media, 'politics':politics, 'all':all})

# def product_detail(request):
#    return render(request, 'app/productdetail.html')

class BlogDetailView(View):
  def get(self,request,pk):
        product = Blog.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',{'Blog':Blog})


def login(request):
   return render(request, 'app/login.html')

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':form})
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registred Successfully')
            form.save() 
        return render(request, 'app/customerregistration.html', {'form':form})

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
 def get(self,request):
    form = BlogerProfileForm()
    return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})

 def post(self, request):
    form = BlogerProfileForm(request.POST)
    if form.is_valid():
        usr = request.user
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        address = form.cleaned_data['address']
        city = form.cleaned_data['city']
        state = form.cleaned_data['state']
        pincode = form.cleaned_data['pincode']
        email = form.cleaned_data['email']
        contact_no = form.cleaned_data['contact_no']
        reg = Bloger(user=usr, first_name=first_name, last_name=last_name, address=address, city=city, state=state, pincode=pincode, email=email, contact_no=contact_no)
        reg.save()
        messages.success(request, 'Congratulations Profile Update Successfully')
    return render(request, 'app//profile.html', {'form':form,'active':'btn-primary'})

'''
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount = amount + shipping_amount
            return render(request, 'app/addtocart.html', {'carts':cart, 'totalamount':totalamount, 'amount':amount})
        else:
            return render(request, 'app/emptycart.html')

@login_required
def buy_now(request):
   return render(request, 'app/buynow.html')

'''

'''
@login_required
def address(request):
    add = Bloger.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add, 'active':'btn-primary'})
@login_required
def orders(request):
    op =OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'order_placed':op})
'''

'''
@login_required
def checkout(request):
  user = request.user
  add = Customer.objects.filter(user=user)
  cart_items = Cart.objects.filter(user=user)
  amount = 2569
  shipping_amount = 70.0
  total_amount = 0.0
  cart_product = [p for p in Cart.objects.all() if p.user == user]
  if cart_product:
        for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount = amount + shipping_amount
  return render(request, 'app/checkout.html', {'add':add, 'totalamount':amount, 'cart_items':cart_items} )

@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")
'''