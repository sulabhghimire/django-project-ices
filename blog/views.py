from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import context #to give HTTP RESPONSES
from .models import Article
from .forms import ArticlePostForm
from django.urls import reverse

from django.contrib import messages

#Class based views sajilo hunxa, override 
#Function based views use

def homepage(request):

    articles    = Article.objects.all().order_by('-date_created')
    

    context     = {
        'posts'  : articles,
    }

    return render(request, 'blog/home.html', context)

def article_details(request, pk):

    article     = Article.objects.get(id=pk)

    context     = {
        'posts'  : article,
    }

    return render(request, 'blog/article_details.html', context)

def post_article(request):

    if request.user.is_authenticated: 
        if request.method == "POST":
            form    = ArticlePostForm(request.POST)
            if form.is_valid():
                data    = form.cleaned_data
                article = Article.objects.create(
                    author  = request.user,
                    title   = data['title'],
                    content = data['content']
                )
                messages.success(request, "Your article was posted sucessfully.")
                return redirect(reverse('article_details', kwargs={'pk' : article.pk}))
            messages.error(request, "Your form is invalid.")

        form    = ArticlePostForm()

        context = {
            'form' : form,
        }

        return render(request, "blog/post.html", context)
    else:
        return redirect("login")


def update_article(request, pk):
    
    form_data   = get_object_or_404(Article, id=pk)

    if request.method == "POST":
        form    = ArticlePostForm(request.POST)
        if form.is_valid():
            data    = form.cleaned_data
            article = form_data
            article.title = data['title']
            article.content = data['content']
            article.save()
            messages.success(request, "Your article was updated sucessfully.")
            return redirect(reverse('article_details', kwargs={'pk' : article.pk}))
        messages.error(request, "Your form is invalid.")

    form    = ArticlePostForm(instance=form_data)

    context = {
        'form' : form,
    }

    return render(request, "blog/update.html", context)

def article_delete(request, pk):

    data   = get_object_or_404(Article, id=pk)

    if request.method == "POST":
        data.delete()
        messages.success(request, "Your article was deleted sucessfully.")
        return redirect(reverse('home'))

    context = {
        'article' : data,
    }

    return render(request, "blog/delete.html", context)

def search(request):

    if request.method == "POST":

        searched_value  = request.POST['searched']

        if searched_value=="":
            return redirect(reverse('home'))
        else:
            articles = Article.objects.filter(title__contains=searched_value).order_by('-date_created')
            context = {
                'searched_title' : searched_value,
                'posts'          : articles,
            }
            return render(request, 'blog/search.html', context)

    return render(request, 'blog/search.html')

# Create your views here.
# ALL YOUR LOGIC GOES HERE