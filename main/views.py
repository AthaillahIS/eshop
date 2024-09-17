from django.shortcuts import render, redirect
from main.forms import OrderEntryForm
from main.models import Entry
from django.http import HttpResponse
from django.core import serializers

def show_xml(request):
    data = Entry.objects.all()
    return HttpResponse(serializers.serialize('xml', data), content_type='aplication/xml')

def show_json(request):
    data = Entry.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='aplication/json')

def show_xml_by_id(request, id):
    data = Entry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml', data), content_type='aplication/xml')

def show_json_by_id(request, id):
    data = Entry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', data), content_type='aplication/json')
    

# Create your views here.
def show_main(request):
    order_entries = Entry.objects.all()
    context = {
        'name' : 'Athaillah Sifa Tanudatar',
        'class' : 'PBP E',
        'npm' : '2306275683',
        'app_name' : 'eshop',
        'order_entries' : order_entries,
    }

    return render(request, "main.html", context)

def add_order_entry(request):
    form = OrderEntryForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    
    context = { 'form' : form }
    return render(request, 'add_order_entry.html', context)