from django.db import models

# Create your models here.

class MinorTrack(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    read_more = models.CharField(max_length=200, unique=True)
    vid_url = models.CharField(max_length=200)
    offered_by = models.CharField(max_length=100)
    tot_creds = models.PositiveSmallIntegerField()
    icon_class = models.CharField(max_length=50)
    syllabus = models.FileField(upload_to='pdfs')


class MTSyllabus(models.Model):
    mt_id = models.ForeignKey(MinorTrack, on_delete=models.CASCADE)
    semester = models.PositiveSmallIntegerField()
    course_code = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    lec = models.PositiveSmallIntegerField()
    creds = models.PositiveSmallIntegerField()