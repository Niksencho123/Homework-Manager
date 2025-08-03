from django.db import models
from datetime import timedelta, date

# Create your models here.
#subject
#teacher
class Subject(models.Model):
    subjectName = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    def __str__(self):
        return self.subjectName

class Assignment(models.Model):
    subjectConn = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assignmentDesc = models.TextField()
    dueDate = models.DateField()

    def __str__(self):
        return self.assignmentDesc
    