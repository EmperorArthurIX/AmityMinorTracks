from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import MTSyllabus, MinorTrack
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django import forms

# Create your views here.

def home(req):
    MT_OBJECTS = list(MinorTrack.objects.all())
    MT_OBJECTS.sort(key=(lambda x : x.name))
    return render(req, 'index.html', {'count': len(MT_OBJECTS), 'cards': MT_OBJECTS[:6], 'open_date': "September 1st, 2022", "open_time": "5:00 PM", "close_time": "5:00 PM", "close_date": "September 2nd, 2022"})


def tracks(req):
    MT_OBJECTS = list(MinorTrack.objects.all())
    MT_OBJECTS.sort(key=(lambda x : x.name))
    return render(req, 'service.html', {'count': len(MT_OBJECTS), 'cards' : MT_OBJECTS})


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
    # if req.method=='POST':

    #     formnumber = req.POST['formnumber']
    #     user = list(filter(lambda x : x.username==formnumber, list(User.objects.all())))
    #     print(formnumber, user)
    #     if user is not None and len(user) == 1:
    #         return render(req, 'about.html')
    #     return render(req, 'login.html', {"data" : "Login Failed"})
    # return render(req, 'login.html')
    return render(req, 'about.html')

def details(req):
    MT_OBJECTS = list(MinorTrack.objects.all())
    MT_OBJECTS.sort(key=(lambda x : x.name))
    MT_READS = [i.read_more for i in MT_OBJECTS]
    if req.GET['track'] in MT_READS:
        track = MT_OBJECTS[MT_READS.index(req.GET['track'])]
        syllabus = MTSyllabus.objects.filter(mt_id_id=track.id)
        return render(req, 'details.html', {'mt': track, 'syllabus': syllabus})
        # return HttpResponse("I will render {} page by passing object to template".format(track.name))


def team(req):
    return render(req, "BigPP.html")


def syllabus(req):
    return redirect("https://mega.nz/folder/SdInBZIL#vw8b7mewAP6lHJQ1tOSuNQ")