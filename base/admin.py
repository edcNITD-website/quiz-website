from django.contrib import admin

# Register your models here.

from .models import Student,Questions,Answer
admin.site.register(Student)

admin.site.register(Questions)
admin.site.register(Answer)



