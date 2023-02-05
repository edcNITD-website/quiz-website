from django.db import models

from django.contrib.auth.models import User

# User= get_user_model

DIFF_CHOICES =(
    ('easy','easy'),
    ('medium','medium'),
    ('hard','hard'),
)


QUESTION_TYPE =(
    ('single_correct','single'),
    ('multi_correct', 'multi'),
    ('text_based','text'),
    
    
)

class Student(models.Model):
    user = models.OneToOneField(User, null =True,on_delete=models.CASCADE)
    #  = models.CharField(max_length=255,null=True)
    school = models.CharField(max_length=255,null=True)
    standard = models.PositiveIntegerField(null=True)
    # city_of_residence = models.CharField(max_length=255,blank=False)
    phone_number=models.PositiveIntegerField(null=True)
    def __str__(self) -> str:
         return "Student "+self.user.first_name +" " + self.user.last_name





class Questions(models.Model):
    

    
    # question = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)
    question_type= models.CharField(max_length=20,choices=QUESTION_TYPE,default='single' )




    def _str_(self):
         return str(self.question)


    def get_answers(self):
            return self.answer_set.all()

class Answer(models.Model):
    text=models.CharField(max_length=255)
    correct=models.BooleanField(default=False)
    question=models.ForeignKey(Questions, on_delete=models.CASCADE)


    def _str_(self):
        return f"question: {self.question.question}, Answer:{self.text}, correct:{self.correct}"

    
    
    




        










        
