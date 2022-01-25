from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import context #to give HTTP RESPONSES
from .models import Article
from .forms import ArticlePostForm
from django.urls import reverse

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
    
    if request.method == "POST":
        form    = ArticlePostForm(request.POST)
        if form.is_valid():
            data    = form.cleaned_data
            article = Article.objects.create(
                author  = request.user,
                title   = data['title'],
                content = data['content']
            )
            return redirect(reverse('article_details', kwargs={'pk' : article.pk}))

    form    = ArticlePostForm()

    context = {
        'form' : form,
    }

    return render(request, "blog/post.html", context)

# Create your views here.
# ALL YOUR LOGIC GOES HERE