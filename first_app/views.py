from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
from . import forms
from first_app.forms import NewTopicForm
# Create your views here.


def index(request):
    webpages_list = Topic.objects.all()
    date_dict = {'topics' : webpages_list }
    # my_dict = {'insert_me': 'Hello from views.py!'}
    return render(request,'first_app/index.html',context=date_dict)

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
