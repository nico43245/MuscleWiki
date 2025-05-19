from django import forms

from exercises.models import Exercise, MuscleGroup
from django.contrib.auth.models import User


class ExerciseForm(forms.ModelForm):
    video_url = forms.URLField(
        label='Video URL',
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Video URL'
        })
    )

    class Meta:
        model = Exercise
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of exercise'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description of exercise'}),
            'difficulty': forms.Select(attrs={'class': 'form-select'}),
            'muscle_group': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean(self):
        cleaned_data=self.cleaned_data
        name = cleaned_data.get('name')

        qs = Exercise.objects.filter(name=name)
        if self.instance and self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            self.add_error('name', 'Există deja un exercițiu cu același nume.')

        return cleaned_data


class ExerciseUpdateForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields='__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of exercise'}),
            'muscle_group': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Muscle Group'}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'Prenume',
            'last_name': 'Nume',
        }


