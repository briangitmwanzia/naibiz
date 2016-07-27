from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from biz.models import *

from django.contrib.auth.decorators import login_required

from django.core.context_processors import csrf


def home_page(request):
    return render(request,'biz/home.html')

def business_page(request):
    
    return render(request,'biz/business_page.html')

def business_signup(request):
    return render(request,'biz/business_signup.html')

def client_page(request):
    biznames=UserProfile.objects.all()
    return render(request,'biz/client_page.html',{ 'biznames':biznames })
    '''
    biznames=bizname.objects.all()
    slugify(biznames)
    return render(request,'biz/client_page.html',{ 'biznames':biznames })
    '''

def biz_item(request):
    biznames=UserProfile.objects.all()
    return render(request,'biz/biz_items.html',{ 'biznames':biznames })

def logedin(request):
    return render(request,'biz/logedin.html')



@login_required
def user_profile(request):
    #if request.method=='POST':
        form=UserProfileForm(request.POST,instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user')
        else:
            user=request.user
            profile=user.profile
            form=UserProfileForm(instance=profile)

        args={}
        args.update(csrf(request))
        args['form']=form
        return render_to_response('biz/profile.html',args)
