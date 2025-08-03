from django import forms

class AssignmentForm(forms.Form):
    classField = forms.CharField(max_length=120)
    teacherField = forms.CharField(max_length=120)
    descField = forms.CharField(widget=forms.Textarea)
    dueField = forms.DateField()

    def send_assignment(self):
        print(f"Added assignment for {self.cleaned_data['classField']}")