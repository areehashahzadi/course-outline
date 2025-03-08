from django.shortcuts import render, redirect
from django.http import Http404
from . import util

def index(request):
    return render(request, "outline/index.html", {
        "topics": util.list_topics()
    })

def topic_page(request, title):
    content = util.get_topic(title)
    if content is None:
        raise Http404("Topic does not exist")
    return render(request, "outline/topic_page.html", {
        "title": title,
        "content": content
    })

def search(request):
    query = request.GET.get('q', '')
    topics = util.search_topics(query)
    return render(request, "outline/search_results.html", {
        "query": query,
        "topics": topics
    })

def new_page(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        if util.save_topic(title, content):
            return redirect("topic_page", title=title)
        else:
            return render(request, "outline/new_page.html", {
                "error": "Topic with this title already exists."
            })
    return render(request, "outline/new_page.html")

def edit_page(request, title):
    content = util.get_topic(title)
    if request.method == "POST":
        new_content = request.POST.get("content", "")
        util.save_topic(title, new_content)
        return redirect("topic_page", title=title)
    return render(request, "outline/edit_page.html", {
        "title": title,
        "content": content
    })

def random_page(request):
    title = util.random_topic()
    return redirect("topic_page", title=title)
