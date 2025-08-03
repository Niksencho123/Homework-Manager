from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='assignments-index'),
    path('thisweek/', views.this_week, name='assignments-thisWeek'),
    path('assignmentNew/', views.newAssignment, name='assignments-newAssignment'),
    path('assignmentSuccess/', views.added_success_view, name='assignments-success')
]
