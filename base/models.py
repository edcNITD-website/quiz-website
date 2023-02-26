from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import uuid

# COUNTDOWN TIMER
class EventDates(models.Model):
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()
    type = models.CharField(max_length=100,default="home");
    name = models.CharField(default="",max_length=100)

    def __str__(self) -> str:
        return self.name + ' starts at : '+self.event_start.isoformat() + ' ends at : '+self.event_end.isoformat()



# User= get_user_modelV

# DIFF_CHOICES =(
#     ('easy','easy'),
#     ('medium','medium'),
#     ('hard','hard'),
# )


# QUESTION_TYPE =(
#     ('single_correct','single'),
#     ('multi_correct', 'multi'),
#     ('text_based','text'),
    
    


class Student(models.Model):
    user = models.OneToOneField(User, null =True,on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=True)
    school = models.CharField(max_length=255,null=True)
    standard = models.PositiveIntegerField(null=True)
    phone_number = models.PositiveIntegerField(null=True)
    city_of_residence = models.CharField(max_length=255,null=False,default="")
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " | " + self.school

# class Questions(models.Model):
    

    
#     # question = models.CharField(max_length=255)
#     
#     




#     def _str_(self):
#          return str(self.question)


#     def get_answers(self):
#             return self.answer_set.all()

# class Answer(models.Model):
#     text=models.CharField(max_length=255)
#     correct=models.BooleanField(default=False)
#     question=models.ForeignKey(Questions, on_delete=models.CASCADE)


#     def _str_(self):
#         return f"question: {self.question.question}, Answer:{self.text}, correct:{self.correct}"





# class question( models.Model):
#     QUESTION_TYPE= (
#         (1, 'radio'),
#         (2, 'checkbox'),
#         (3, 'text'),
#     )
    
# class questions(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     text = models.CharField(max_length=2048, null=False, blank=False)
#     question_type= models.CharField(max_length=20,choices=QUESTION_TYPE,default='radio' )
#     difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES,default='easy')
#     correct = models.BooleanField(default=False)
#     # rank = models.SmallIntegerField(default=0)

# class Answer(models.Model):
#     user = models.OneToOneField(User, null =True,on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
#     choice = models.ForeignKey(questions, null=True, on_delete=models.DO_NOTHING)
#     free_text = models.CharField(max_length=2048, null=True, blank=True)
  

# class BaseModel(models.Model):
#     uid = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, null=False)
 


#     class Meta:
#         abstract =True

  

    
    
# class Category(BaseModel):
#     category_name =models.CharField(max_length=255)
#     created_at =models.DateField(auto_now_add=True)
#     updated_at= models.DateField(auto_now=True)


#     def __str__(self) -> str:
#         return self.category_name 



# class  Question(BaseModel):
#     category =models.ForeignKey(Category ,related_name='category',on_delete=models.CASCADE)
#     question = models.CharField(max_length=255)
#     marks =models.IntegerField(default=10)

#     def __str__(self) -> str:
#         return self.question

# class Answer(BaseModel):
#     question =models.ForeignKey(Question, related_name='question_answer',on_delete=models.CASCADE)
#     answer =models.CharField(max_length=100,default=" ")    
#     is_correct =models.BooleanField(default=False)


#     def __str__(self) -> str:
#         return self.answer


        










        
