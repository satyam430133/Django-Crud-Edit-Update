from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def Home(request):
    return render(request,'index.html')

def Registration(request):
    if request.method == 'POST':
        names = request.POST.get('name')
        phones = request.POST.get('phone')
        Stu.objects.create(Name=names,Phone=phones)
        return redirect('show')
    
def ShowData(request):
    shh = Stu.objects.all()
    return render(request,'show.html',{'shh':shh})

def EditData(request,pk):
    stut = Stu.objects.get(id=pk)
    return render(request,'update.html',{'stut':stut})

def UpdateData(request,pk):
    st =Stu.objects.get(id=pk)
    st.Name=request.POST.get('name')
    st.Phone=request.POST.get('phone')
    st.save()
    return redirect('show')
