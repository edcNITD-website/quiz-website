from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import csv, datetime
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
    context['has_started'] = Status.objects.first().has_started
    return render(request,'base/home.html', context)

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
def quiz_home(request):
    if StartTime.objects.filter(student=Student.objects.filter(user=request.user).first()).first() is not None and StartTime.objects.filter(student=Student.objects.filter(user=request.user).first()).first().quiz_over == True:
        return redirect('/quiz-over')
    if request.method == 'POST':
        if StartTime.objects.filter(student=Student.objects.filter(user=request.user).first()).first() is None:
            start_time = StartTime(start_time=datetime.datetime.now(), student=Student.objects.filter(user=request.user).first())
            start_time.save()
        return redirect('/quiz/1')
    return render(request, 'base/quiz_home.html', { 'has_started': Status.objects.first().has_started })

@login_required
def quiz(request, sno):
    time = StartTime.objects.filter(student=Student.objects.filter(user=request.user).first()).first()
    if Status.objects.first().has_started == False:
        return redirect('/')
    if time and time.quiz_over == True:
        return redirect('/quiz-over')
    else:
        if (datetime.datetime.now(datetime.timezone.utc) - time.start_time).seconds // 60 > 45:
            time.quiz_over = True
            time.save()
    if request.method == 'GET':
        paragraph_q = Paragraph.objects.filter(sno=sno).first()
        mcq_q = Mcq.objects.filter(sno=sno).first()
        answer = Answer.objects.filter(student=Student.objects.filter(user=request.user).first(), sno=sno).first()
        max_sno = 0
        for i in Paragraph.objects.all():
            max_sno = max(max_sno, int(i.sno))
        for i in Mcq.objects.all():
            max_sno = max(max_sno, int(i.sno))
        max_sno_list = []
        for i in range(1, max_sno + 1):
            if Answer.objects.filter(student=Student.objects.filter(user=request.user).first(), sno=i).first() and Answer.objects.filter(student=Student.objects.filter(user=request.user).first(), sno=i).first().response != '':
                max_sno_list.append({
                    'answered': 'True',
                    'index': i
                })
            else:
                max_sno_list.append({
                    'answered': 'False',
                    'index': i
                })
        if paragraph_q is not None:
            return render(request, 'base/quiz.html', { 'question': paragraph_q, 'type': 'paragraph', 'student_response': answer, 'max_sno': max_sno_list, 'start_time': time.start_time })
        elif mcq_q is not None:
            return render(request, 'base/quiz.html', { 'question': mcq_q, 'type': 'mcq', 'student_response': answer, 'max_sno': max_sno_list, 'start_time': time.start_time })
        else:
            return redirect('/quiz/1')
    else:
        student = Student.objects.filter(user=request.user).first()
        response = request.POST['response']
        question_id = request.POST['question_id']
        paragraph_q = Paragraph.objects.filter(sno=sno).first()
        mcq_q = Mcq.objects.filter(sno=sno).first()
        already_answered = Answer.objects.filter(question_id=question_id,student=student).first()
        if already_answered is not None:
            already_answered.response = response
            if paragraph_q is not None:
                if paragraph_q.correct_answer == response:
                    already_answered.is_correct = True
                else:
                    already_answered.is_correct = False
            else:
                if mcq_q.correct_option == response:
                    already_answered.is_correct = True
                else:
                    already_answered.is_correct = False
            already_answered.save()
        else:
            answer = Answer(student=student, response=response, question_id=question_id, sno=sno)
            if paragraph_q is not None:
                if paragraph_q.correct_answer == response:
                    answer.is_correct = True
                else:
                    answer.is_correct = False
            else:
                if mcq_q.correct_option == response:
                    answer.is_correct = True
                else:
                    answer.is_correct = False
            answer.save()
        new_sno = int(sno) + 1
        return redirect('/quiz/' + str(new_sno))

def export(request):
    if request.user.username == 'admin':
        students = Student.objects.all()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename= quizregistration.csv'
        writer = csv.writer(response)
        writer.writerow(['Name','Email','Standard','School','Phone Number','City of Residence'])
        # field =['User','Standard','School','Phone Number','City of Residence']
        # student_fields= students.values_list('name','email','standard','school','phone_number','city_of_residence')
        for student in students:
            writer.writerow(
                    [
                        student.user.first_name + " " + student.user.last_name,
                        student.user.email,
                        student.standard,
                        student.school,
                        student.phone_number,
                        student.city_of_residence
                    ]
                )
        return response

@login_required
def standings(request):
    if Leaderboard.objects.first().show == True:
        all_students = Student.objects.all()
        context = []
        for student in all_students:
            score = 0
            answers = Answer.objects.filter(student=student).all()
            for answer in answers:
                if answer.is_correct == True:
                    score += 10
            context.append({
                'student': student,
                'score': score
            })
        context.sort(key=lambda x: score, reverse=True)
        return render(request, 'base/standings.html', { 'standings': context })
    else:
        return redirect('/')

def quizOver(request):
    if request.method == 'POST':
        time = StartTime.objects.filter(student=Student.objects.filter(user=request.user).first()).first()
        time.quiz_over = True
        time.save()
        return redirect('/quiz-over')
    return render(request, 'base/quiz_over.html')
