from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.http import require_POST

# Create your views here.
# * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 *

def cart(request):
    cart_items = CartItem.objects.all()
    cart_items_list = []
    for item in cart_items:
        cart_items_list.append(str(item))
    print(cart_items_list)
    return render(request, 'pages/cart.html', {'cart_items': cart_items})


# @csrf_exempt
# def create_cart_item(request):
#     if request.method == 'POST':
#         title_id = request.POST.get('title')
#         quantity = request.POST.get('quantity')
#         if not title_id or not quantity:
#             return JsonResponse({'success': False, 'message': 'Invalid request'})
#         try:
#             title = Product.objects.get(id=title_id)
#         except Product.DoesNotExist:
#             return JsonResponse({'success': False, 'message': 'Invalid product'})
#         cart_item = CartItem.objects.create(title=title, quantity=quantity)
#         return JsonResponse({'success': True, 'cart_item_id': cart_item.id})
#     return JsonResponse({'success': False, 'message': 'Invalid request'})

@csrf_exempt
@require_POST
def create_cart_item(request):
    data = json.loads(request.body)
    product_id = data.get('product_id')
    decrement_quantity = data.get('decrement_quantity', False)

    if not product_id:
        return JsonResponse({'success': False, 'message': 'Product ID is required'})

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Product not found'})

    if decrement_quantity and product.quantity > 0:
        product.quantity -= 1
        product.save()

    cart_item, created = CartItem.objects.get_or_create(
        title=product,
        defaults={'total_price': product.price}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.update_total_price()

    return JsonResponse({'success': True, 'message': 'Product added to cart'})


# * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 * * 8 *


def home(request):
    if request.method == 'POST':
        # print(request.POST)
        body = request.POST
        new_product = Product.objects.create(
            title = body['title'], 
            quantity = body['quantity'], 
            price = body['price'], ) #.....
        selected_categories = body.getlist('category')
        for category in selected_categories:
            new_product.categories.add(
                Category.objects.get(title=category))
        new_product.save()
        return redirect('home')

    product_info = [] 
    products = Product.objects.prefetch_related('categories')
    product_info.clear() # new ## ## ## ### # # ## # # #
    for product in products:
        # print(product.categories.all().values())
        product_info.append({
            'product': product,
            'category': product.categories.all()
        })
    # print(product_info)
    return render(request, 'pages/layout_2.html', {"products":product_info, 'nested':True})

def products_by_category(request, id):
    category = Category.objects.get(id = id)
    data = {
        # 'products': Category.objects.get(id=id).product.all(),
        'products': category.product.all(),
        'title?': category,
        'nested': False
    }
    return render(request, 'pages/layout_2.html', data)

@csrf_exempt
def product(request, id):
    try:
        my_product = Product.objects.all().get(id=id)
        product_info = []
        if request.method == 'GET':
            product = Product.objects.prefetch_related('categories').get(id=id)
            product_info.append({
                'product': product,
                'category': product.categories.all()
            })
            return render(request, 'pages/layout_2.html', {"products": product_info, 'nested': True})
        if request.method == 'PUT':
            body = json.loads(request.body)
            print(body)
            my_product.quantity = body['quantity']
            my_product.save()
            # pass #### commented out the pass
        if request.method == 'DELETE':
            my_product.delete() ###### added ()
            # return redirect('home')
            return render(request, 'pages/layout_2.html', {"products":product_info, 'nested':True})
        return JsonResponse({'success': True})
    
    except Exception as e:
        print(e)
        return JsonResponse({'success': False})