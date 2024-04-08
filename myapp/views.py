from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *


def seller_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        Seller.objects.create(username=username, email=email, password=password)
        return redirect('seller_login')
    context = {'current_page': 'seller_register'}
    return render(request, 'seller_registration.html', context)

def seller_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            seller = Seller.objects.get(username=username, password=password)
            return redirect('seller_home')  
        except Seller.DoesNotExist:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'seller_login.html', {'error_message': error_message})
    else:
        context = {'current_page': 'seller_login'}
        return render(request, 'seller_login.html', context)

def buyer_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        Buyer.objects.create(username=username, email=email, password=password)
        return redirect('buyer_login')
    context = {'current_page': 'buyer_register'}
    return render(request, 'buyer_registration.html', context)

def buyer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            buyer = Buyer.objects.get(username=username, password=password)
            # Perform any authentication logic here
            return redirect('buyer_home')  # Redirect to buyer home page after successful login
        except Buyer.DoesNotExist:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'buyer_login.html', {'error_message': error_message})
    else:
        context = {'current_page': 'buyer_login'}
        return render(request, 'buyer_login.html', context)

@login_required
def seller_home(request):
    # Retrieve products uploaded by the currently logged-in seller
    seller_products = Product.objects.filter(seller=request.user)
    if seller_products.exists():
        return render(request, 'seller_home.html', {'seller_products': seller_products})
    else:
        return render(request, 'blank_seller_home.html')

def buyer_home(request):
    # Retrieve all posts made by sellers
    seller_posts = Product.objects.filter(seller__isnull=False)
    return render(request, 'buyer_home.html', {'seller_posts': seller_posts})

def upload_product(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        product_name = request.POST['product_name']
        product_image = request.FILES['product_image']
        description = request.POST['description']
        price = request.POST['price']
        
        # Save the product to the database
        product = Product.objects.create(
            seller=request.user,
            company_name=company_name,
            product_name=product_name,
            product_image=product_image,
            description=description,
            price = price
        )
        return redirect('seller_home')
    return render(request, 'upload_product.html')

@login_required
def buy_post(request, post_id):
    product = Product.objects.get(pk=post_id)
    product.bought = True
    product.save()
    return redirect('buyer_home')

@login_required
def add_to_cart(request, post_id):
    product = get_object_or_404(Product, pk=post_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        # If the item is already in the cart, increase its quantity
        cart_item.quantity += 1
        cart_item.save()

    return redirect('buyer_home')

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'view_cart.html', {'cart_items': cart_items})

@login_required
def buy_now(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        # Validate form data
        address = request.POST.get('address')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        alt_phone = request.POST.get('alt_phone')
        state = request.POST.get('state')
        city = request.POST.get('city')
        house_no = request.POST.get('house_no')
        area = request.POST.get('area')
        nearby = request.POST.get('nearby')
        option_choice = request.POST.get('option_choice')

        if not (address and name and phone and state and city and house_no and area and nearby and option_choice):
            # If any required field is not provided, display an error message or handle it as needed
            return render(request, 'buy_now.html', {'product': product, 'error_message': 'All fields are required'})

        # Create the order
        order = Order.objects.create(
            user=request.user,
            product=product,
            name=name,
            phone=phone,
            alt_phone=alt_phone,
            state=state,
            city=city,
            house_no=house_no,
            area=area,
            nearby=nearby,
            address=address,
            option_choice=option_choice
        )
        return redirect('order_confirmation', order_id=order.id)
    return render(request, 'buy_now.html', {'product': product})

@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'order_confirmation.html', {'order': order})


def logout_view(request):
    logout(request)
    return redirect('login')