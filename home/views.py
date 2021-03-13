from django.shortcuts import render
from .models import Estate
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    estate= Estate.objects.all()
    context = {'estates':estate}
    return render(request,"estates/index.html",context)

def estate_list(request):
    estate_list = Estate.objects.all()
    paginator = Paginator(estate_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"estates":page_obj}
    return render(request,"estates/estate_list.html",context)

def estate_detail(request,slug):
    estate_detail=Estate.objects.get(slug=slug)
    context={"estate_detail":estate_detail}
    return render (request,"estates/estate_detail.html",context)



