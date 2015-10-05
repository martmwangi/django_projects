from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
#        fields = ['full_name','email','age']
        exclude = ['last_update']
        model = Student
    def clean_age(self):
        age = self.cleaned_data.get('get')
        if age >120
            raise forms.ValidationError("You may be too old for this class")

        return age
