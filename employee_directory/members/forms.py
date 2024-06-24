from django import forms
from .models import Member

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'



class Employee_Edit_Form(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['timeline', 'address']