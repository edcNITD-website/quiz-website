from django.contrib import admin
from .models import Student, EventDates, Paragraph, Mcq, Answer, Status, Leaderboard, StartTime

admin.site.register(Student)
admin.site.register(EventDates)
admin.site.register(Paragraph)
admin.site.register(Mcq)
admin.site.register(Answer)
admin.site.register(Status)
admin.site.register(Leaderboard)
admin.site.register(StartTime)
