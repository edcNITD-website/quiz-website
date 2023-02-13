from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#COUNTDOWN
# from .models import Student
from .models import *
from django.utils import timezone
# Create your views here.
def home(request):
    context = {}
    event_dates = EventDates.objects.filter(type="home").order_by('-event_start').first()
    # print(event_dates)
    msg = "Esummit has ended"
    time_diff = -1
    end = True
    if event_dates is not None:
        current_time = timezone.now()
        time_diff = 0
        end = False
        if event_dates.event_start > current_time:
            # hunt is yet to begin
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











# def home(request):
#     return render(request, 'base/home.html')

@login_required
def register(request):
    user= request.user
    if request.method == 'POST':
        name= request.POST['Name']
        standard =request.POST['standard']
        school = request.POST['School']
        phone_number= request.POST['Phone']
        city=request.POST['City']
        



        if Student.objects.filter(user=request.user).first() is not None:
            
            student = Student.objects.filter(user=request.user).first()
            student.user = user
                                                                                                                        
            student.standard = standard
            student.school = school
            student.phone_number=phone_number
            
            student.save()
        else:    
            student = Student.objects.create( standard=standard,phone_number=phone_number,school= school)
            student.save()

            # student_model=  Student.objects.get(name=name)
            new_profile= Student.objects.create(user=request.user,standard=standard,phone_number=phone_number,school=school)
            
        return render (request, 'base/home.html')


    else:
            return render(request, 'base/profile.html')


@login_required
def quiz(request):
    return render(request, 'base/quiz.html')


