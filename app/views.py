from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import MTSyllabus, MinorTrack
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django import forms

# Create your views here.

def home(req):
    MT_OBJECTS = MinorTrack.objects.all()
    return render(req, 'index.html', {'cards': MT_OBJECTS[:6]})


def tracks(req):
    MT_OBJECTS = MinorTrack.objects.all()
    return render(req, 'service.html', {'cards' : MT_OBJECTS})


#### DEBUG VERSION OF LOGIN FUNCTION: Needs login html head script to be updated to show results
# def login(req):
#     if req.method=='POST':
#         #test data

#         formnumber = req.POST['formnumber']
#         password = req.POST['password']
#         print(formnumber, password)
#         user = list(filter(lambda x : x.username==formnumber,list(User.objects.all())))
#         data = {}
#         if user and len(user) == 1:
#             user = user[0]
#             data["username"] = "User exists"
#             if user.check_password(password+"\r"):
#                 data["password"] = "Password Matches"
#                 return render(req, 'about.html')
#             if user.has_usable_password():
#                 data["usable"] = "Usable"
#             data["password"] = "Password does not match"
#         # print(list(filter(lambda x: x.username==formnumber, list(User.objects.all())))[0].password)
#         data["login_fail"] = "Login Failed"
#         return render(req, 'login.html', {"data" : data})
#     return render(req, 'login.html')


def login(req):
    if req.method=='POST':

        formnumber = req.POST['formnumber']
        password = req.POST['password']
        user = list(filter(lambda x : x.username==formnumber,list(User.objects.all())))
        if user and len(user) == 1:
            user = user[0]
            if user.check_password(password):
                return render(req, 'about.html')
        return render(req, 'login.html', {"data" : "Login Failed"})
    return render(req, 'login.html')

def details(req):
    MT_OBJECTS = MinorTrack.objects.all()
    MT_READS = [i.read_more for i in MT_OBJECTS]
    if req.GET['track'] in MT_READS:
        track = MT_OBJECTS[MT_READS.index(req.GET['track'])]
        syllabus = MTSyllabus.objects.filter(mt_id_id=track.id)
        return render(req, 'details.html', {'mt': track, 'syllabus': syllabus})
        # return HttpResponse("I will render {} page by passing object to template".format(track.name))


def team(req):
    return render(req, "BigPP.html")