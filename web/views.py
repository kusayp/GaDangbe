from django.shortcuts import render

# Create your views here.

def index(request):
    context={
        'title':'Ga-Dangbe'
    }
    return render(request, 'index.html',context=context)

def about(request):
    context={
        'title':'Ga-Dangbe'
    }
    return render(request, 'index.html',context=context)

def event(request):
    context={
        'title':'Ga-Dangbe'
    }
    return render(request, 'index.html',context=context)

def gallery(request):
    context={
        'title':'Ga-Dangbe'
    }
    return render(request, 'index.html',context=context)

def subgroup(request):
    context={
        'title':'Ga-Dangbe'
    }
    return render(request, 'index.html',context=context)

def alumini(request):
    context={
        'title':'Ga-Dangbe'
    }
    return render(request, 'index.html',context=context)