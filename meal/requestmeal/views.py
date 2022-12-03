from django.shortcuts import render
from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, ClaimForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from .models import Student, NYUEATS, AvaiableStuff
from django.db.models import F


def home(request):
    return render(request, 'requestmeal/home.html')

def about(request):
    return render(request, 'requestmeal/about.html')

def register(request):
    if request.method == 'POST':  
        form = RegistrationForm(request.POST)
        if form.is_valid():
           form.save()
           #save user info
    else:
      form = RegistrationForm()
    return render(request, 'requestmeal/register.html', {'form': form})

@login_required
def menu(request):
    the_student = Student.objects.filter(user_id = request.user.id)
    index = request.user.email.index("@")
    net_id = request.user.email[:index]
    the_student.update(SID= net_id)
    return render(request, 'requestmeal/menu.html',{'the_student' : the_student})


@login_required
def profile(request):
    cd = 1
    if request.method == 'POST':
        Student.objects.filter(user_id = request.user.id).update(MSallotment=F("MSallotment") + 1)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        cd = request.POST.get('access')
        if u_form.is_valid():
            u_form.save()
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
        'cd': cd
    }

    return render(request, 'requestmeal/profile.html', context)


def admintwo(request):
    if request.method == 'POST':
        MSAvail = 0
        DDAvail = 0
        for i in range (1, 4):
            MSAvail += NYUEATS.objects.get(id = i).MSP
            MSAvail -= NYUEATS.objects.get(id = i).MSU
            DDAvail += NYUEATS.objects.get(id = i).DDP
            DDAvail -= NYUEATS.objects.get(id = i).DDU
        AvaiableStuff.objects.filter(id = 1).update(MS=MSAvail)
        AvaiableStuff.objects.filter(id = 1).update(DD=DDAvail)

    return render(request, 'requestmeal/admintwo.html')

def adminpage(request):
    data = NYUEATS.objects.all()
    num = 0
    for each in Student.objects.all():
        if each.access == 1:
            num += 1
    return render(request, 'requestmeal/adminpage.html', {'data': data, 'num': num})

def list(request):
    student_list = Student.objects.all()
    return render(request, 'requestmeal/list.html',
                    {'student_list' : student_list})


@login_required
def claim(request):
    the_student = Student.objects.filter(user_id = request.user.id)
    if request.method == 'POST':
        a_form = ClaimForm(request.POST)
        cd = request.POST.get('MS')
        cdd = request.POST.get('DD')
        Student.objects.filter(user_id = request.user.id).update(MSallotment=F("MSallotment") - cd)
        Student.objects.filter(user_id = request.user.id).update(DDallotment=F("DDallotment") - cdd)
        if a_form.is_valid():
            a_form.save()
    else:
        a_form = ClaimForm()
    context = {
        'the_student' : the_student,
        'a_form': a_form,
    }

    return render(request, 'requestmeal/claim.html', context)

def requestlist(request):
    list = Student.objects.all()
    num = 0
    for each in list:
        if each.access == 1:
            num += 1
    if request.method == 'POST':
        acc = request.POST.get("action") 
        if acc == "accept":
            Student.objects.filter(SID = request.POST.get("SID")).update(access = 2)
        elif acc == "deny":
            Student.objects.filter(SID = request.POST.get("SID")).update(access = 0)
        #if request.POST.get('access'):
            #s = request.POST.get('access')
            #s.save()
    return render(request, 'requestmeal/requestlist.html', {'list': list, 'num': num})

def studentlist(request):
    list = Student.objects.all()
    num = 0
    for each in list:
        if each.access == 1:
            num += 1
    return render(request, 'requestmeal/studentlist.html', {'list': list, 'num': num})

def adminaccept(request):
    stuff = AvaiableStuff.objects.all()

    return render(request, 'requestmeal/adminaccept.html', {'stuff': stuff})

def adminlogin(request):
    return render(request, 'requestmeal/adminlogin.html')