from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm
from django.contrib import auth
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist


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
        "item":x,
        'type':"view"
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
    
    
def snippets_delete(request,value):
    x = Snippet.objects.get(id = value)
    x.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def log_out(request):
    auth.logout(request)
    return redirect('home')

def login_page(request):
   if request.method == 'POST':
       username = request.POST.get("username")
       password = request.POST.get("password")
       # print("username =", username)
       # print("password =", password)
       user = auth.authenticate(request, username=username, password=password)
       if user is not None:
           auth.login(request, user)
       else:
           # Return error message
           pass
   return redirect('home')

def snippets_edit(request,value):
    try:
        snipet = Snippet.objects.get(id=value)
    except ObjectDoesNotExist:
        raise Http404
    if request.method == "GET":

        context = {
            "item":snipet,
            'type' :"edit"
        }
        return render(request,"pages/snipett_page.html",context)
    else:
        form_date = request.POST
        snipet.name = form_date["name"]
        snipet.code = form_date['code']
        snipet.creation_date = form_date["creation_date"]
        snipet.save()
        return redirect('list')