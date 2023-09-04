from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {'pagename': 'Добавление нового сниппета',
                "form":form}
        return render(request, 'pages/add_snippet.html', context)
    else:
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            return render(request,'pages/add_snippet.html',{'form': SnippetForm()})

def snippets_list(request):
    x = Snippet.objects.all()
    context = {'pagename': 'Просмотр сниппетов',"snipet":x}
    return render(request, 'pages/view_snippets.html', context)

def snippets_page(request,value):
    x = Snippet.objects.get(id = value)
    context = {
        "item":x
    }
    return render(request,"pages/snipett_page.html",context)

def snippets_create(request):
    if request.method == "POST":
        name = request.POST['name']
        lang = request.POST['lang']
        code = request.POST["code"]
        snippet = Snippet(name=name,lang=lang,code=code)
        snippet.save()
        return redirect('list')