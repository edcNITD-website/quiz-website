from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('register', views.register),
    path('export', views.export),
    path('quiz', views.quiz_home),
    path('quiz/<sno>', views.quiz),
    path('standings', views.standings),
    path('quiz-over', views.quizOver),
]