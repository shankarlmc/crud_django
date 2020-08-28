from django.shortcuts import render, HttpResponseRedirect
from .models import Blog
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MyForm, MyRegister


# Create your views here.


def Home(request):
    posts = Blog.objects.all()
    context_home = {
        'posts': posts,
    }
    return render(request, 'home/index.html', context_home)


@login_required(login_url='/login')
def Add(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # author = MyForm.changed_data.get('author')
            messages.success(request, f"New Blog Post Added !")
            return HttpResponseRedirect('add')
    else:
        form = MyForm()

    context = {
        'form': form,
    }
    return render(request, 'home/add.html', context)


def View(request, slug):
    posts = Blog.objects.get(slug=slug)
    context_post = {
        'posts': posts,
    }
    return render(request, 'home/details.html', context_post)


@login_required(login_url='/login')
def Update(request, id):
    post = Blog.objects.get(id=id)
    form = MyForm(instance=post)
    # pass the object as instance in form
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    context_post = {
        'form': form,
    }
    return render(request, 'home/add.html', context_post)


@login_required(login_url='/login')
def Delete(request, id):
    post = Blog.objects.get(id=id)
    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect("/")
    context_post = {
        'post': post,
    }
    return render(request, 'home/delete.html', context_post)


def Login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/add')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/add')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'home/login.html', context)


def Register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/add')
    else:
        form = MyRegister()
        if request.method == 'POST':
            form = MyRegister(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return HttpResponseRedirect('/login')

        context = {
            'form': form,
        }
        return render(request, 'home/register.html', context)

# def Register(request):
#     return render(request,'home/register.html')
