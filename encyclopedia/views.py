import markdown2
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title=None):
    if title:
        content = util.get_entry(title)
        if content is None:
            return HttpResponseNotFound('<h1>Page not found</h1>')
        else:
            html_content = markdown2.markdown(content)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_content
            })
    else:
        # If no title is provided, return the index page
        return index(request)


def search(request):
    query = request.GET.get('q', '')
    entries = util.list_entries()
    if query in entries:
        return redirect('entry', title=query)
    else:
        matching_entries = [entry for entry in entries if query.lower() in entry.lower()]
        return render(request, "encyclopedia/search_results.html", {
            "entries": matching_entries,
            "query": query
        })


def new_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        entries = util.list_entries()
                
        if title.lower() in (entry.lower() for entry in entries):
            return render(request, "encyclopedia/new_page.html", {
                "error": "An entry with this title already exists.",
                "title": title,
                "content": content
            })
        else:
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry", kwargs={'title': title}))    
   
    return render(request, "encyclopedia/new_page.html")


def edit_page(request, title):
    content = util.get_entry(title)
    if request.method == "POST":
        new_content = request.POST.get("content")
        util.save_entry(title, new_content)
        return HttpResponseRedirect(reverse("entry", kwargs={'title': title}))
    return render(request, "encyclopedia/edit_page.html", {"title": title, "content": content})


def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return HttpResponseRedirect(reverse("entry", kwargs={'title': random_entry}))