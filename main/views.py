

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from yahoo_fin import stock_info as si 
import pandas as pd
import requests 
import time
import queue
from django.http import HttpResponse

from django.contrib.auth import get_user_model
from main.models import Plans,Device,UserSubscription

User = get_user_model()



@login_required
def home(request):  
    if request.method=="POST":
        print("home",request.data)


    data = Plans.objects.all()
    print(data)


    return render(request,"home.html",{"data":data})



@login_required
def profile(request):  

    if request.method == "POST":
       dt =  UserSubscription.objects.get(username=request.user.username)
       dt.plan_status = False
       dt.save()
      
       print(dt.plan_status)

    
    user_data = User.objects.filter(id=request.user.id)[0]

    if user_data:
        return HttpResponse("No Subscriptions")
    subsc_data = UserSubscription.objects.filter(user = user_data)[0]
    plan_data = Plans.objects.filter(id=subsc_data.plan.id)[0]
    
    
    return render(request,"profile.html",{"usr":subsc_data,"sub":plan_data})









@login_required
def payment(request):
    if request.method=="POST":
        print(request.POST)
        plan_data = Plans.objects.filter(name=request.POST['plan_details'])[0]
        price = ""
        typ = request.POST["bill_cycle"]
        if typ=="monthly":
            price = plan_data.price_m
        else:
            price = plan_data.price_y


        data = {"plan":plan_data.name,"price":price,"period":typ}
       
        

    
    return render(request,"payment.html",{"data":data})




@login_required
def confirm(request,pk):
    user_id = request.user.id
    idx = pk.index("-")
    plan_type = pk[:idx]
    plan_period = pk[idx+1:]
    username = User.objects.get(id=user_id)
    sub = UserSubscription.objects.filter(username=request.user.username)

    selected_plan = Plans.objects.filter(name=plan_type)[0]
    prc = 0
    if plan_period=="monthly":
        prc = selected_plan.price_m
    else:
        prc = selected_plan.price_y
    
    print(plan_type,plan_period,sub,selected_plan)


    if len(sub)==0:
        cre = UserSubscription.objects.create(
            username = request.user.username,
            user = request.user,
            plan_status = True,
            plan = Plans.objects.filter(name=plan_type)[0],
            price = prc
        )
        cre.save()
        print("success")
    else:
        
        upd = UserSubscription.objects.get(username=request.user.username)
        upd.plan_status = True
        
        upd.price = prc
        upd.save()
        


    print(selected_plan.device.all())
    devices = ""
    for each in selected_plan.device.all():
        if devices=="":
            devices+=each.name
        else:
            aa = "+"+each.name
            devices+= aa
        
    print(devices)
    subscr = ""

    sub = UserSubscription.objects.filter(username=request.user.username)

    if len(sub)==0:
        subscr = "None"
    else:
        if sub[0].plan_status == True:
            subscr = "Active"
        else:
            subscr = "Cancelled"

    data = UserSubscription.objects.get(username=request.user.username)
    return render(request,"confirm.html",{"data":data,"pln":selected_plan,"status":subscr,"dev":devices})



    




