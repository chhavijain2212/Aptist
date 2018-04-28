from django.shortcuts import render
from .models import *

global stream
global correct
correct = []
global questions
global q
global s
s=0
# Create your views here.


def index(request):
    return render(request, 'home.html', {'streams': Stream.objects.all()})


def ques(request, qid):
    global questions
    global q
    qu = questions[qid]
    q = qid
    return render(request, 'indexQ.html', {'q': qu})


def mark(request):
    r = request.POST.get('answer')
    global q
    global correct
    global s
    if r == questions[q].opcorrect:
        correct.append(questions[q])
    q += 1
    if q == questions.count():
        sum = 0
        for st in correct:
            if st.type == 'd' or st.type == 'D':
                sum += 1
            else:
                sum += 3
        print(sum)
        if sum < (s*3/5):
            mssg = 'Are you sure you want to continue this stream?'
        else:
            mssg = 'You are good. Continue if you like this stream.'
        return render(request, 'result.html', {'mssg': mssg, 'result': sum})

    return render(request, 'indexQ.html', {'q': questions[q]})


def instructions(request,sid):
    global stream
    global questions
    global s
    stream = sid
    for st in Stream.objects.filter(pk=sid):
        questions = st.questions_set.all().order_by('?')[:7]
    for k in questions:
        if k.type=='d' or k.type=='D':
            s+=1
        else:
            s+=3
    return render(request, 'instructions.html', {'s': s})