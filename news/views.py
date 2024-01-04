from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category
from .forms import CategoryForm, NewsForm


def home(request):
    news_list = News.objects.all()
    return render(request, 'home.html', {'news_list': news_list})


def news_details(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, 'news_details.html', {'news': news})


def categories_form(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Category.objects.create(**data)
            return redirect('home-page')
    else:
        form = CategoryForm()
        context = {"form": form}

    return render(request, 'categories_form.html', context)


def news_form(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            categories = data.pop('categories')
            news = News.objects.create(**data)
            news.categories.set(categories)
            return redirect('home-page')
    else:
        form = NewsForm()
        categories = Category.objects.all()
        context = {"form": form, "categories": categories}

    return render(request, 'news_form.html', context)
