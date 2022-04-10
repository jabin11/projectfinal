from django.shortcuts import render,HttpResponse
from web_app .models import Index
# Create your views here.
def index(request) :
    if request.method == 'POST':
            index = Index()
            name = request.POST.get('name')
            email = request.POST.get('email')
            date = request.POST.get('date')
            phone = request.POST.get('phone')
            index.name=name
            index.email=email
            index.date=date
            index.phone=phone
            index.save()
    return render(request,'index.html')