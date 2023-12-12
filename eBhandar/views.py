from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Product, CartItem, Contact, Order, Career
from math import ceil
from django.contrib.auth.models import User, auth 

def index(request):
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    cart_items = CartItem.objects.filter(user=request.user.id) 
    item_count= cart_items.count() 

    return render(request, 'index.html', {'allProds':allProds,"item_count":item_count})


def searchMatch(query, item):
    if query.lower() in item.decs.lower() or query.lower() in item.product_name.lower() or query.lower() in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    cart_items = CartItem.objects.filter(user=request.user.id) 
    item_count= cart_items.count() 
    return render(request, 'search.html', {'allProds':allProds,"item_count":item_count})



def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user) 
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})    

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect("/")

def dec_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity -= 1
    if cart_item.quantity == 0:
        cart_item.delete()
        return redirect('/view_cart')
    cart_item.save()
    return redirect("/view_cart")

def inc_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect("/view_cart")

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('/view_cart')


def contact(request):
    if request.method=='POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request, 'contact.html')


def prodView(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'prodView.html', {'product':product[0]})

def prodView_add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('PruductView', myid=product.id)

def checkout(request):
    if request.method=='POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        landmark = request.POST.get('landmark', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')

        # Fetch cart items
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        # Convert cart items to a list for JSONField
        cart_items_list = [{'product_name': item.product.product_name, 'quantity': item.quantity} for item in cart_items]

        order = Order(name=name, email=email, phone=phone, landmark=landmark, address1=address1, address2=address2, city=city, state=state, zip_code=zip_code, cart_items=cart_items_list, order_amount=total_price)
        order.save()

        cart_items.delete()
        id=order.order_id
    cart_items = CartItem.objects.filter(user=request.user) 
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price})   



def signup(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":
            first_name=request.POST["first_name"]
            last_name=request.POST["last_name"]
            email=request.POST["email"]
            # role=request.POST["role"]
            password=request.POST["password"]
            confirm_pass=request.POST["confirm_pass"]
            if password==confirm_pass:
                User.objects.create_user(first_name=first_name, last_name=last_name ,email=email, username=email,password=password)
                # , role=role
                return redirect("/login")
            else:
                return redirect("/signup")
        else:
            return render(request,"signup.html")

def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user= auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            return redirect("/login")

    return render(request, 'login.html')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect("/")

def account(request):
    return render(request, 'account.html')

def about(request):
    return render(request, 'about.html')

def orders(request):
    return render(request, 'orders.html')

def tracker(request):
    return render(request, 'tracker.html')

def thanks(request):
    return render(request, 'thanks.html')

def shop_index(request):
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    cart_items = CartItem.objects.filter(user=request.user.id) 
    item_count= cart_items.count() 

    return render(request, 'shop_index.html', {'allProds':allProds,"item_count":item_count})

def profile(request):
    return render(request, 'profile.html')

def address(request):
    return render(request, 'address.html')    

def vegetable(request):
    return render(request, 'vegetable.html')

def career(request):
    if request.method=='POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        qual = request.POST.get('qual', '')
        skill = request.POST.get('skill', '')
        desc = request.POST.get('desc', '')
        contact = Career(name=name, email=email, phone=phone, qual=qual, skill=skill, desc=desc)
        contact.save()
    return render(request, 'career.html')