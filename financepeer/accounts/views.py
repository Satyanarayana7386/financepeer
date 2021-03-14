from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from accounts.forms import DocumentForm
from accounts.models import UserData
from django.core.serializers import serialize
from django.core.paginator import Paginator
from django.urls import reverse_lazy

import json

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

def detail(request):

    # ss = UserData.objects.order_by('userId')
    # ss  = UserData.objects.values('userId')
    # ss = UserData.objects.filter(userId=1)
    user_list = UserData.objects.all()

    return render(request, 'accounts/details.html', {'user_list': user_list})




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def model_form_upload(request):
    if request.method == 'POST':

        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            data = handle_uploaded_file(request.FILES['document'])
            check_user_list = UserData.objects.all()

            if len(check_user_list) >= 0:
                for idx, user in enumerate(data):
                    user = UserData.objects.create(**user)
                    user.save()
                form.author = request.user.username
                form.save()
                return redirect('index')
            else:
                return redirect('index')
            # return reverse_lazy('index')
    else:
        form = DocumentForm()

    return render(request, 'accounts/file_upload.html', {
        'form': form
    })


def handle_uploaded_file(f):
    json_data = {}
    with open('media/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            json_data = json.loads(chunk)
        return json_data
