from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name' : 'Baguette',
        'price' : '19.500',
        'description' : 'Best Baguette in the WORLD!!',
        'rating' : '5',
        'date' : '11-08-2024',
        'author_name' : 'Athaillah Sifa Tanudatar',
        'author_class' : 'PBP E',
        'app_name' : 'eshop',
    }

    return render(request, "main.html", context)