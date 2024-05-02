from django.contrib.auth import logout
from django.core.mail import message
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .utils import get_mongodb
from .forms import TagForm, QuoteForm, AuthorForm
from .models import Tag, Author

def logout_view(request):
    message.info(request, 'You have logout')
    logout(request)
    return redirect('/')

def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/author.html', {'form': form})

    return render(request, 'quotes/author.html', {'form': AuthorForm()})

def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/tag.html', {'form': form})

    return render(request, 'quotes/tag.html', {'form': TagForm()})

def add_quote(request):
    tags = Tag.objects.all()
    auths = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_note = form.save()
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_note.tags.add(tag)

            au = Author.objects.get(fullname=request.POST.get('author'))
            au.quotes_set.add(new_note, bulk=False)

            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/note.html', {"tags": tags, "authors": auths, 'form': form})

    return render(request, 'quotes/note.html', {"tags": tags, "authors": auths, 'form': QuoteForm()})
