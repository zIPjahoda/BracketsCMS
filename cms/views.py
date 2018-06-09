from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect

from .models import Article, Category, StaticPage


# Create your views here.
def test(request):
    return redirect("http://google.com/")


# Vypis clanku
def post_detail(request, url):
    post = get_object_or_404(Article, url=url)
    return render(request, 'cms/post-detail.html', {'post': post})


# Vypis kategorie + clanky
def category_detail(request, url):
    post = get_object_or_404(Category, url=url)
    article_all = Article.objects.all()
    return render(request, 'cms/category-detail.html', {'post': post, 'article_all': article_all})


def home(request):
    return render(request, "cms/homepage.html")


def page_detail(request, url):
    item = get_object_or_404(StaticPage, url=url)
    return render(request, "cms/static-page.html", {
        "item": item
    })



