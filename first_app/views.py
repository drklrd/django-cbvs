from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
from . import forms
from first_app.forms import NewTopicForm,UserForm,UserProfileInfoForm
# Create your views here.


from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

from django.views.generic import View
from django.http import HttpResponse

class CBView(View):

    def get(self,request):
        return HttpResponse("Class based views")

def index(request):
    webpages_list = Topic.objects.all()
    date_dict = {'topics' : webpages_list }
    # my_dict = {'insert_me': 'Hello from views.py!'}
    return render(request,'first_app/index.html',context=date_dict)

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        print('$$$',username)
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else :
                return HttpResponse("Account not active")
        else:
            print("Login failed !")
            return HttpResponse("invalid login details provided")

    else:
        return render(request,'first_app/login.html',{})

@login_required # only if user is logged in we do logout. so adding this decorator
def user_logout(request):

    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'first_app/registration.html',
                    {
                    'user_form':user_form,
                    'profile_form' : profile_form,
                    'registered' : registered
                    })

def other(request):
    return render(request,'first_app/other.html')

def relative(request):
    return render(request,'first_app/relative.html')

def form_name_view(request):

    form = NewTopicForm()

    if request.method == 'POST':
        form = NewTopicForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error form invalid')

    return render(request,'first_app/form_page.html',{'form':form})

    # form = forms.FormName()
    #
    # if request.method == 'POST':
    #     form = forms.FormName(request.POST)
    #
    #     if form.is_valid():
    #         print("Validaion")
    #         print("NAME " + form.cleaned_data['name'])
    #
    # return render(request,'first_app/form_page.html',{'form':form})
