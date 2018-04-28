from django.db import models

# Create your models here.

class Stream(models.Model):
    stream = models.CharField(max_length=150)
    img = models.FileField(default="")
    def __str__(self):
        return self.stream

class Questions(models.Model):
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    ques = models.CharField(max_length=5000)
    op1 = models.CharField(max_length=1000)
    op2 = models.CharField(max_length=1000)
    op3 = models.CharField(max_length=1000)
    op4 = models.CharField(max_length=1000)
    opcorrect = models.CharField(max_length=1)
    type = models.CharField(max_length=1,default='D')
    def __str__(self):
        return str(self.pk)+" in "+str(self.stream)