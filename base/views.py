from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.contrib.auth.models import User
from .models import Student




# Create your views here.







def home(request):
    return render(request, 'base/home.html')

@login_required
def register(request):
    user= request.user
    if request.method == 'POST':
        # name = request.POST['name']
        standard =request.POST['standard']
        school = request.POST['school']
        phone_number= request.POST['phone_number']
        



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
            



    else:
            return render(request, 'base/profile.html')


# @login_required
def quiz(request):
    return render(request, 'base/quiz.html')


