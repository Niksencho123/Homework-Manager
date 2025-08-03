from django import forms
from .models import Subject

class AssignmentForm(forms.Form):
    classField = forms.ChoiceField(choices=[])
    descField = forms.CharField(widget=forms.Textarea)
    dueField = forms.DateField()

    def send_assignment(self):
        print(f"Added assignment for {self.cleaned_data['classField']}")
    
    def __init__(self, *args, **kwargs):
        super(AssignmentForm, self).__init__(*args, **kwargs)
        self.fields['classField'].choices = [(subject.id, subject.subjectName) for subject in Subject.objects.all()]