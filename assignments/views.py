from django.shortcuts import render, redirect
from .models import Assignment
from .forms import AssignmentForm
from datetime import date, timedelta
from django.utils import timezone

# Create your views here.
def index(request):
    today = date.today()
    tomorrow = today + timedelta(days=1) 

    assignments = Assignment.objects.filter(dueDate=tomorrow)
    context = {'assignments': assignments, 'tomorrow': True}
    return render(request, 'assignments/index.html', context)

def this_week(request):
    today = date.today()
    tomorrow = today + timedelta(days=1) 
    start_of_week = today - timedelta(days=today.weekday())  # Monday
    end_of_week = start_of_week + timedelta(days=6)          # Sunday

    assignmentsDue = Assignment.objects.filter(dueDate=tomorrow)
    assignmentsLate = Assignment.objects.filter(dueDate__range=(start_of_week, today))
    assignmentsLater = Assignment.objects.filter(dueDate__range=(tomorrow + timedelta(days=1), end_of_week))
    context = {'assignmentsDue': assignmentsDue,'assignmentsLate': assignmentsLate, 'assignmentsLater': assignmentsLater, 'thisWeek': True}
    return render(request, 'assignments/thisWeek.html', context)

def newAssignment(request):
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            newAssignmentAdded = Assignment(subject=form.cleaned_data['classField'], teacher=form.cleaned_data['teacherField'], assignmentDesc = form.cleaned_data['descField'], dueDate = form.cleaned_data['dueField'])
            newAssignmentAdded.save()
            return redirect('assignments-success')
    else:
        form = AssignmentForm()
    context = {
        'form': form,
        'addHomework': True
    }
    return render(request, 'assignments/new.html', context)

def added_success_view(request):
    return render(request, 'assignments/added_success.html')