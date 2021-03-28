from django.shortcuts import render
from .models import place,blog
# Create your views here.
def fun(request):
    # obj=place()
    # obj.name="Kerala"
    # obj.price=200
    # obj.desc="This is Kerala"
    obj=place.objects.all()
    obj1=blog.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})