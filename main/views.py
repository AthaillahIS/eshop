from django.shortcuts import render, redirect
from main.forms import OrderEntryForm
from main.models import Entry
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

def show_xml(request):
    data = Entry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('xml', data), content_type='aplication/xml')

def show_json(request):
    data = Entry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', data), content_type='aplication/json')

def show_xml_by_id(request, id):
    data = Entry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml', data), content_type='aplication/xml')

def show_json_by_id(request, id):
    data = Entry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', data), content_type='aplication/json')
    

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    context = {
        'name' : request.user.username,
        'class' : 'PBP E',
        'npm' : '2306275683',
        'app_name' : 'eshop',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def add_order_entry(request):
    form = OrderEntryForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        order_entry = form.save(commit=False)
        order_entry.user = request.user
        order_entry.save()
        return redirect('main:show_main')
    
    context = { 'form' : form }
    return render(request, 'add_order_entry.html', context)

def edit_order(request, id):
    order = Entry.objects.get(pk = id)

    form = OrderEntryForm(request.POST or None, instance=order)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_order.html", context)

def delete_order(request, id):
    order = Entry.objects.get(pk = id)
    order.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
@require_POST
def add_order_entry_ajax(request):
    item_name = strip_tags(request.POST.get("item_name"))  # strip HTML tags!
    description = strip_tags(request.POST.get("description"))  # strip HTML tags!
    price = request.POST.get("price")
    rating = request.POST.get("rating")
    user = request.user

    new_order = Entry(
        item_name=item_name, price=price,
        description=description, rating=rating,
        user=user
    )
    new_order.save()
    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def create_mood_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_mood = Entry.objects.create(
            user=request.user,
            item_name=data["item_name"],
            price=int(data["price"]),
            description=data["description"],
            rating=int(data["rating"]),
            # date=datetime.now()
        )

        new_mood.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)