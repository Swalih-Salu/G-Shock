from django.shortcuts import render,redirect
from .models import Sitedetails
from .form import SiteForm
# Create your views here.
def Home(req):
    obj=Sitedetails.objects.all()
    return render(req,'index.html',{"Sitedetails":obj})


def details(req,new1_id):
    data=Sitedetails.objects.get(id=new1_id)
    return render(req,"details.html",{'data':data})


def Regnew(req):
    if req.method=='POST':
        name=req.POST.get('name')
        rating=req.POST.get('rating')
        desc=req.POST.get('desc')
        image=req.FILES['image']
        price=req.POST.get('price')
    
        new=Sitedetails(name=name,rating=rating,desc=desc,image=image,price=price)
        new.save()
        return redirect("/")
    return render (req,'regnew.html')

def delete(req,new2_id):
    if req.method=='POST':
        data=Sitedetails.objects.get(id=new2_id)
        data.delete()
        return redirect("/")
    return render(req,'delete.html')

def update(req,new3_id):
    upd=Sitedetails.objects.get(id=new3_id)
    form=SiteForm(req.POST or None,req.FILES,instance=upd)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(req,'update.html',{'form':form,'upd':upd})