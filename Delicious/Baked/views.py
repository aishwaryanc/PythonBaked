from django.shortcuts import render
from .forms import Contactform, registerform, loginform
from .models import Contact, registeration
from Baked import models

# Create your views here.

def home(request):
    return render(request, 'homepages/index.html')

def login(request):
    return render(request, 'homepages/login.html')


def register(request):
    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            Name = userObj['Name']
            Email = userObj['Email']
            Password = userObj['Password']
            Confirmpass = userObj['Confirmpass']
            if Password == Confirmpass:
                form.save()
                return render(request, 'homepages/login.html')

            else:
                # raise forms.ValidationError('Looks like a username with that email or password already exists')
                return render(request, 'homepages/register.html')
    else:
        form = registerform()
    return render(request, 'homepages/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = loginform(request.POST)
        users = registeration.objects.all()
        if form.is_valid():
            userObj = form.cleaned_data
            email = userObj['Email']
            password = userObj['Password']
            for user in users:
                while user.Email == email and user.Password == password:
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.Name
                    request.session['user_email'] = user.Email
                    return render(request, 'homepages/index.html')
    else:
        form = loginform()
    return render(request, 'homepages/login.html', {'form': form})

def contact(request):
    form = Contactform(request.POST , request.FILES)
    if form.is_valid():
        form.save()
        return render(request, 'homepages/index.html')
    return render(request, 'homepages/contact.html', {'form': form})

def view(request):
    # users = registeration.objects.all()
    # return render(request, 'homepages/view.html', {'users': users})
    users = Contact.objects.all()
    return render(request, 'homepages/view.html', {'users': users})

def updatecontact(request,id):
    user = Contact.objects.get(id=id)
    form = Contactform(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        users = Contact.objects.all()
        return render(request, 'homepages/view.html', {'users':users})
    return render(request, 'homepages/editcontact.html', {'form': form, 'user': user})

def deletecontact(request,id):
    user = Contact.objects.get(id=id)
    users = Contact.objects.all()
    user.delete()
    return render(request,'homepages/view.html', {'user': user, 'users': users})