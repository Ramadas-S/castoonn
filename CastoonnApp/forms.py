from django import forms
from .models import CreatorUserProfile

class CreatorUserProfileForm(forms.ModelForm):

    gender = forms.ChoiceField(choices=[
        ('Gender', 'Gender'),
        ('Female', 'Female'),
        ('Male', 'Male'),
    ], widget=forms.Select(attrs={'class': 'form-control item', 'id': 'Gender', 'placeholder': 'Gender'}))
    
    profession = forms.ChoiceField(choices=[
        ('Profession', 'Profession'),
        ('Actor', 'Actor'),
        ('Costume_Designer', 'Costume_Designer'),
        # Add more choices as needed
    ], widget=forms.Select(attrs={'class': 'form-control item', 'id': 'profession', 'placeholder': 'Profession'}))

    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control item', 'id': 'birthday', 'placeholder': 'Date of Birth'}))



    class Meta:
        model = CreatorUserProfile
        fields = ['name', 'lastname', 'nickname', 'gender', 'phone_number', 'email', 'profession', 'experience']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Lastname'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Nickname'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control item','placeholder':'phone number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control item','placeholder':'Email'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control item','placeholder':'Experience'})
        }
       
