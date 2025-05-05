from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from exercises.forms import ExerciseForm
from exercises.models import MuscleGroup, Exercise


class MuscleGroupListView(ListView):
    template_name='exercises/list_muscle_group.html/'
    model = MuscleGroup
    context_object_name = 'groups'


class ExerciseListView(ListView):
    template_name='exercises/list_exercises.html/'
    model = Exercise
    context_object_name = 'exercises'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Exercise.objects.filter(muscle_group__slug=slug)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['group'] = MuscleGroup.objects.get(slug=self.kwargs.get('slug'))
        return context

class ExerciseDetailView(DetailView):
    model = Exercise
    template_name ='exercises/exercises_detail.html'
    context_object_name = 'exercise'

class ExerciseCreateView(LoginRequiredMixin, CreateView):
    template_name = 'exercises/exercises_add.html'
    model = Exercise
    form_class = ExerciseForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        data['exercise']=Exercise.objects.all()
        return data


    def get_success_url(self):
        return reverse_lazy('exercise-list', kwargs={'slug': self.object.muscle_group.slug})


class ExerciseUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'exercises/exercises_add_update.html'
    model = Exercise
    form_class = ExerciseForm

    def get_success_url(self):
        slug = self.object.muscle_group.slug
        return reverse_lazy('exercise-list', kwargs={'slug': slug})



class ExerciseDeleteView(LoginRequiredMixin, DeleteView):
    model = Exercise
    template_name = 'exercises/exercise_confirm_delete.html'
    success_url = reverse_lazy('muscle-group-list')




