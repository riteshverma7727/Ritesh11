from django.shortcuts import render,HttpResponse

# Create your views here.
def index1(request):
    return render(request,'pollsapp/index.html')