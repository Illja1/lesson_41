from django.shortcuts import render
from .models import Categories,Note



def nav(request):
    categories = Categories.objects.all()
    return render(request, 'notes/landing.html', {'categories': categories})

def note_by_category(request, category_title):
    category = Categories.objects.get(title=category_title)
    note = Note.objects.filter(category=category)
    context = {
        'category': category,
        'note': note
    }
    return render(request, 'notes/categories.html', context)