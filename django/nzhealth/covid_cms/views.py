from django.shortcuts import render, redirect
from covid_cms.forms import ReferralForm
from covid_cms.models import Referral
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html', {})

@login_required
def emp(request):  
    if request.method == "POST":  
        form = ReferralForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ReferralForm()  
    return render(request,'emp.html',{'form':form})  

@login_required
def show(request):  
    referrals = Referral.objects.all()  
    return render(request,"show.html",{'referrals':referrals})  

@login_required
def edit(request, id):  
    referral = Referral.objects.get(id=id)  
    return render(request,'edit.html', {'referral':referral}) 

@login_required 
def update(request, id):  
    referral = Referral.objects.get(id=id)  
    form = ReferralForm(request.POST, instance = referral)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'referral': referral})

@login_required 
def destroy(request, id):  
    referral = Referral.objects.get(id=id)  
    referral.delete()  
    return redirect("/show")  