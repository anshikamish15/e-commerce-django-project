from django.shortcuts import render, redirect
from learn.models import UserProfile
from .models import Category, Product


# Create your views here.
def home(request):
    uObj = UserProfile.objects.get(user__username=request.user)
    return render(request, "welcomeseller.html", {'data' : uObj})

def add_product(request):
    uObj = UserProfile.objects.get(user__username=request.user)
    uOBj1 = Category.objects.all()

    if request.method == "POST":
        a = request.POST['pro_name']
        b = request.POST['pro_desc']
        c = request.POST['pro_price']
        d = request.FILES['pro_img']
        e = request.POST['pro_qty']
        f = request.POST['pro_cat']

        present = False

        for i in uOBj1:
            if( f == i.catName ):
                present = True


        if(present == True):
            h = Category.objects.get(id=f)
            pro_obj = Product(name=a, desc=b, price=c, pro_img=d, qty=e, category=h, added_by=uObj)
            pro_obj.save()
        else:
            ac = Category(catName=f)
            ac.save()

            j = Category.objects.get(catName=f)
            pro_obj = Product(name=a, desc=b, price=c, pro_img=d, qty=e, category=j, added_by=uObj)
            pro_obj.save()

        

    return render(request, "addproduct.html", {'data' : uObj, 'catObj' : uOBj1,})