from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import csv
from .models import *
from django.utils import timezone

# Create your views here.
def home(request):
    context = {}
    event_dates = EventDates.objects.filter(type="home").order_by('-event_start').first()
    msg = "Esummit has ended"
    time_diff = -1
    end = True
    if event_dates is not None:
        current_time = timezone.now()
        time_diff = 0
        end = False
        if event_dates.event_start > current_time:
            time_diff = (event_dates.event_start - current_time).total_seconds()
            msg = "QUIZ Starts in"
        elif event_dates.event_end > current_time:
            time_diff = (event_dates.event_end - current_time).total_seconds()
            msg = "QUIZ Ends in"
        else:
            time_diff = (event_dates.event_end - current_time).total_seconds()
            msg = "QUIZ has ended"
            end = True
    context['msg'] = msg
    context['time_diff'] = int(time_diff)
    context['has_ended'] = end
    return render(request,'base/home.html',context)

@login_required
def register(request):
    user= request.user
    if request.method == 'POST':
        name= request.POST['Name']
        standard =request.POST['Class']
        school = request.POST['School']
        phone_number= request.POST['Phone']
        city=request.POST['City']
        if Student.objects.filter(user=request.user).first() is not None:
            student = Student.objects.filter(user=request.user).first()
            student.user = user
            student.name = name
            student.standard = standard
            student.school = school
            student.phone_number = phone_number
            student.city_of_residence = city
            student.save()
        else:
            new_profile = Student.objects.create(user=request.user, standard=standard, phone_number=phone_number, school=school, name=name, city_of_residence=city)
            new_profile.save()
        return redirect('/')
    else:
        student_details = Student.objects.filter(user=request.user).first()
        return render(request, 'base/profile.html', { 'student_details': student_details })

@login_required
def quiz(request):
    return render(request, 'base/quiz.html')

def export(request):
    if request.user.username == 'admin':
        students = Student.objects.all()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename= quizregistration.csv'
        writer = csv.writer(response)
        writer.writerow(['User','Standard','School','Phone Number','City of Residence'])
        field =['User','Standard','School','Phone Number','City of Residence']
        student_fields= students.values_list('user','standard','school','phone_number','city_of_residence')
        for student in student_fields:
            writer.writerow(student)
        return response
