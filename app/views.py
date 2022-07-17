from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import MTSyllabus, MinorTrack
from django.contrib.auth.models import User, auth
from django.contrib import messages

# GLOBAL DATABASE FETCHED VARIABLES

MT_OBJECTS = MinorTrack.objects.all()
MT_READS = [i.read_more for i in MT_OBJECTS]

# Create your views here.

def home(req):
    return render(req, 'index.html', {'cards': MT_OBJECTS[:6]})


def tracks(req):
    return render(req, 'service.html', {'cards' : MT_OBJECTS})


def login(req):
    if req.method=='POST':
        #test data

        formnumber = req.POST['formnumber']
        password = req.POST['password']
        
        user = auth.authenticate(username=formnumber, password=password)
        if user:
            auth.login(req, user)
            return render(req, 'about.html')

        # messages.info(req, "Incorrect Login Credentials")

        # if req.POST['formnumber'] == '8765432' and req.POST['password'] == '1234':
        #     return render(req, 'about.html')
        return render(req, 'login.html')
    return render(req, 'login.html')


def details(req):
    if req.GET['track'] in MT_READS:
        track = MT_OBJECTS[MT_READS.index(req.GET['track'])]
        syllabus = MTSyllabus.objects.filter(mt_id_id=track.id)
        return render(req, 'details.html', {'mt': track, 'syllabus': syllabus})
        # return HttpResponse("I will render {} page by passing object to template".format(track.name))


def team(req):
    return render(req, "BigPP.html")