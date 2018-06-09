from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.forms.widgets import PasswordInput
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from cms.models import MenuItem, Article, Category, StaticPage
from .forms import ArticleForm, CategoryForm, MenuItemForm, StaticPageForm, UserLoginForm, UserRegisterForm
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .url_generator import generate_url
import logging


# Create your views here.
@login_required
def index(request):
    return render(request, "admin/admin-index.html", {
        "title": "Title page",
        "newest_posts": Article.objects.all()[:5],
        "user_last_login": request.user.last_login
    })


@login_required
def navigation_overview(request):
    navigation_items = MenuItem.objects.all()
    return render(request, "admin/navigation.html", {
        "title": "Navigation management",
        "items": navigation_items,
    })


@login_required
def api_get_next_nav_item_id(request):
    try:
        return HttpResponse(MenuItem.objects.latest("id").id + 1)
    except:
        item = MenuItem(title="", link="")
        item.save()
        item_id = item.pk
        item.delete()
        return HttpResponse(item_id)


@csrf_exempt
@login_required
def api_add_nav_item(request):
    if request.method == "POST":
        form = MenuItemForm(request.POST)
        if form.is_valid():
            nav_item = form.save(commit=False)
            nav_item.save()
        else:
            return HttpResponse(form.errors)
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@csrf_exempt
@login_required
def api_add_empty_nav_item(request):
    item = MenuItem(title="", link="")
    item.save()
    return HttpResponse(True)


@csrf_exempt
def api_edit_nav_item(request, item_id):
    if request.method == "POST":
        nav_item = MenuItem.objects.get(pk=item_id)
        nav_item.title = request.POST["title"] if request.POST["title"] else nav_item.title
        nav_item.link = request.POST["link"] if request.POST["link"] else nav_item.link
        nav_item.save()
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@login_required
def api_delete_nav_item(request, item_id):
    try:
        item = MenuItem.objects.get(pk=item_id)
        item.delete()
    except ObjectDoesNotExist:
        return HttpResponse()
    return HttpResponse()


# Create new Article/Post
@login_required
def post_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.url = generate_url(post.title)
            post.save()
            return redirect('post_detail', url=post.url)
    else:
        form = ArticleForm()
    return render(request, 'admin/post-edit.html', {'form': form, "title": "Nový příspěvek"})


# Edit exist Article/Post
@login_required
def post_edit(request, url):
    post = get_object_or_404(Article, url=url)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.url = generate_url(post.title)
            post.save()
            return redirect('post', url=post.url)
    else:
        form = ArticleForm(instance=post)
    return render(request, 'admin/post-edit.html', {'form': form})


@login_required
def post_delete(request, url):
    item = Article.objects.filter(url=url)
    if item:
        item.delete()
        messages.add_message(request, messages.INFO, "The article has been successfully removed.")
    return redirect("post_overview")


@login_required
def post_detail(request, url):
    post = get_object_or_404(Article, url=url)
    return render(request, 'cms/post-detail.html', {'post': post})


@login_required
def post_overview(request):
    return render(request, "admin/post-overviews.html", {
        "pages": Article.objects.all(),
        "title": "all Article"
    })


@login_required
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.url = generate_url(post.title)
            post.author = request.user
            post.save()
            return redirect('cms_admin-base', url=post.url)
        else:
            return HttpResponse("The data didn't validate!")
    else:
        form = CategoryForm()
    return render(request, 'admin/create-category.html', {'form': form, "title": "Vytvoření nové Kategorie"})


@login_required
def category_edit(request, url):
    post = get_object_or_404(Category, url=url)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.url = generate_url(post.title)
            post.author = request.user
            post.save()
            return redirect('category_detail', url=post.url)
    else:
        form = CategoryForm(instance=post)
    return render(request, 'admin/create-category.html', {'form': form})


@login_required
def category_delete(request, url):
    item = Category.objects.filter(url=url)
    if item:
        item.delete()
        messages.add_message(request, messages.INFO, "The category has been successfully removed.")
    return redirect("category_overview")


@login_required
def category_overview(request):
    return render(request, "admin/category-overviews.html", {
        "pages": Category.objects.all(),
        "title": "all Category"
    })


@login_required
def category_detail(request, url):
    post = get_object_or_404(Category, url=url)
    article_all = Article.objects.all()
    return render(request, 'cms/category-detail.html', {'post': post, 'article_all': article_all})


@login_required
def new_static_page(request):
    if request.method == "POST":
        item_form = StaticPageForm(request.POST)
        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.publish_date = timezone.now()
            item.generate_url()
            item.author = request.user
            item.save()
            return redirect("/cms-admin/static-page/overview")
        else:
            return HttpResponse("The data didn't validate!")
    else:
        form = StaticPageForm()
        return render(request, "admin/create-static-page.html", {
            "form": form,
            "title": "Add a static page",
        })


@login_required
def static_page_overview(request):
    return render(request, "admin/static-page-overview.html", {
        "pages": StaticPage.objects.all(),
        "title": "Static pages"
    })


@login_required
def static_page_delete(request, url):
    item = get_object_or_404(StaticPage, url=url)
    if item:
        item.delete()
        messages.add_message(request, messages.INFO, "The page has been successfully removed.")
    return redirect("static_page_overview")


@login_required
def static_page_detail(request, url):
    item = get_object_or_404(StaticPage, url=url)
    return render(request, "admin/static-page-detail.html", {
        "page": item,
        "title": item.title + " - Static page"
    })


@login_required
def static_page_edit(request, url):
    post = get_object_or_404(StaticPage, url=url)
    if request.method == "POST":
        form = StaticPageForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.generate_url()
            post.author = request.user
            post.save()
            messages.add_message(request, messages.INFO, "The page has been edited successfully!")
        else:
            messages.add_message(request, messages.ERROR, "The form did not validate!")
    else:
        form = StaticPageForm(instance=post)
        return render(request, "admin/create-static-page.html", {
            'form': form,
            'title': "Edit a static page."
        })
    return redirect("static_page_overview")


def login(request):
    if request.POST:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                auth.login(request, user)
                messages.add_message(request, messages.SUCCESS, "Logged in successfully.")
                if request.GET["next"]:
                    return redirect(request.GET["next"])
                else:
                    return redirect("index")
            else:
                messages.add_message(request, messages.ERROR, "The username or password are incorrect.")
                return redirect("user_login")
        else:
            messages.add_message(request, messages.ERROR, "The data received was invalid. Please, try again")
            return redirect("user_login")
    else:
        form = UserLoginForm()
        return render(request, "admin/login.html", {
            "form": form
        })


@login_required
def register(request):
    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            if not (form.cleaned_data["password"] == form.cleaned_data["password_again"]):
                messages.add_message(request, messages.ERROR, "The entered passwords did not match!")
                return redirect("user_register")
            user = form.create_user_object()
            user.save()
            messages.add_message(request, messages.SUCCESS, "Your account has been successfully created.")
            return redirect("index")
        else:
            messages.add_message(request, messages.ERROR, "The data are invalid.")
            return render(request, "admin/register.html", {
                "form": form,
            })
    else:
        form = UserRegisterForm()
        return render(request, "admin/register.html", {
            "form": form
        })


def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.SUCCESS, "Logged out successfully.")
    return redirect("/")
