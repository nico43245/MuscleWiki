from django import forms

from exercises.models import Exercise, MuscleGroup


class ExerciseForm(forms.ModelForm):
    muscle_group = forms.ModelChoiceField(
        MuscleGroup.objects.all().order_by('name'),
        empty_label='Alege grupa…',
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Grupă Musculară',
    )

    class Meta:
        model = Exercise
        fields='__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Name of exercise'}),
            'muscle_group': forms.TextInput(attrs={'class': 'form-control','placeholder':'Muscle Group'}),
            'description': forms.TextInput(attrs={'class': 'form-control','placeholder':'Description of exercise'}),
            'difficulty': forms.TextInput(attrs={'class': 'form-control','placeholder':'Difficulty of exercise'}),

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
