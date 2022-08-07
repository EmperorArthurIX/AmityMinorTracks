from django.contrib import admin
from .models import MTSyllabus, MinorTrack
from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required

# Register your models here.

class FileUploadForm(forms.Form):
    CSV_File = forms.FileField()


@staff_member_required
def upload_csv(req):

    if req.method == "POST":
        file = req.FILES['CSV_File']
        data = file.read().decode('utf-8')
        csv_data = data.split('\n')[1:]
        objs = list()
        for row in csv_data:
            fields = row.split(',')
            # print(fields)
            if len(fields) == 2:
                user = User()
                user.email = str(fields[0])
                if str(fields[1]).endswith('\r'):
                    fields[1] = fields[1][:-1]
                user.username = str(fields[1])
                # if str(fields[2]).endswith('\r'):
                #     fields[2] = fields[2][:-1]
                    # print(fields[2])
                # user.set_password(str(fields[2]))
                # print(user.check_password(str(fields[2])))
                # print(user.has_usable_password())
                objs.append(user)
        # print(objs)
        User.objects.bulk_create(objs=objs)
        return render(req, 'success.html', {"count": len(objs), "name": "Users"})

    form = FileUploadForm()
    return render(req, 'csv_upload.html', {"form": form})


@staff_member_required
def upload_syllabus(req):

    def syllabus_split(row):
        row = str(row)
        row = row.split('"')
        if len(row) == 1:
            return row
        fields = []
        fields.extend(row[0].split(','))
        fields.append(row[1])
        fields.extend(row[2].split(','))
        fields = list(filter(lambda x : x != '',fields))
        return fields

    if req.method == "POST":
        file = req.FILES['CSV_File']
        data = file.read().decode('utf-8')
        csv_data = data.split('\n')[1:]
        objs = list()
        MT_OBJECTS = MinorTrack.objects.all()
        MT_READS = [i.read_more for i in MT_OBJECTS]
        for row in csv_data:
            fields = syllabus_split(row)
            # print(fields)
            if len(fields) == 6:
                syllabus = MTSyllabus()
                try:
                    track = MT_OBJECTS[MT_READS.index(fields[0])]
                    # print(track)
                except Exception as exp:
                    print(exp)
                    track = None
                if track is not None:
                    syllabus.mt_id = track
                    syllabus.semester = fields[1]
                    syllabus.course_code = fields[2]
                    syllabus.title = str(fields[3])
                    syllabus.lec = fields[4]
                    if str(fields[5]).endswith("\r"):
                        fields[5] = fields[5][:-1]
                        # print(fields[5])
                    syllabus.creds = fields[5]
                    objs.append(syllabus)
                    # print(syllabus.mt_id, syllabus.semester, syllabus.course_code, syllabus.title, syllabus.lec, syllabus.creds)
        # print(objs)
        MTSyllabus.objects.bulk_create(objs=objs)
        return render(req, 'success.html', {"count": len(objs), "name": "Syllabus Rows"})

    form = FileUploadForm()
    return render(req, 'syllabus_upload.html', {"form": form})

admin.site.register(MinorTrack)
admin.site.register(MTSyllabus)