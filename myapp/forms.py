from django import forms

class StudentForm(forms.Form):

    name=forms.CharField()

    course=forms.CharField()

    fees=forms.IntegerField()