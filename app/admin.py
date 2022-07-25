from django.contrib import admin
from .models import MTSyllabus, MinorTrack
from django.urls import path
from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User, auth


# Register your models here.

class FileUploadForm(forms.Form):
    CSV_File = forms.FileField()


def upload_csv(req):

    if req.method == "POST":
        file = req.FILES['CSV_File']
        data = file.read().decode('utf-8')
        csv_data = data.split('\n')[1:]
        objs = list()
        for row in csv_data:
            fields = row.split(',')
            print(fields)
            if len(fields) == 3:
                user = User()
                user.email = fields[0]
                user.username = fields[1]
                user.set_password(fields[2])
                objs.append(user)
        # print(objs)
        User.objects.bulk_create(objs=objs)
        return render(req, 'user_success.html', {"count": len(objs)})

    form = FileUploadForm()
    return render(req, 'csv_upload.html', {"form": form})


admin.site.register(MinorTrack)
admin.site.register(MTSyllabus)