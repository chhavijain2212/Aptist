from django.urls import path
from . import views

app_name = 'apti'

urlpatterns = [
    path('ques/<int:qid>', views.ques, name='questions'),
    path('mark', views.mark, name='mark'),
    path('ins/<int:sid>', views.instructions, name='instructions'),
    path('', views.index, name='home'),
]
