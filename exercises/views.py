from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from exercises.forms import ExerciseForm
from exercises.models import MuscleGroup, Exercise
from .forms import UserProfileForm
from django.views.generic import TemplateView
import random



class MuscleGroupListView(ListView):
    template_name='exercises/list_muscle_group.html/'
    model = MuscleGroup
    context_object_name = 'groups'


class ExerciseListView(ListView):
    model = Exercise
    template_name = 'exercises/list_exercises.html'
    context_object_name = 'exercises'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            group = get_object_or_404(MuscleGroup, slug=slug)
            return group.exercises.all()
        return Exercise.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        if slug:
            ctx['current_group'] = get_object_or_404(MuscleGroup, slug=slug)
        else:
            ctx['current_group'] = None
        return ctx

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


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'exercises/profile.html'
    context_object_name = 'profile_user'

    def get_object(self):
        return self.request.user

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'exercises/profile_edit.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('profile')

class WorkoutGeneratorView(LoginRequiredMixin, TemplateView):
    template_name = 'workout_result/workout_result.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx['goals']  = ['Slăbire','Forță','Definire','Rezistență']
        ctx['levels'] = ['Începător','Intermediar','Avansat']

        params = self.request.GET
        if all(k in params for k in ('gender','age','goal','level')):
            gender = params['gender']
            age    = params['age']
            goal   = params['goal']
            level  = params['level']

            exercises = {
                'slăbire': [
        'Burpees',
        'Mountain Climbers',
        'Jumping Jacks',
        'Plank',
        'Squats',
        'High Knees',
        'Jump Rope',
        'Skater Jumps',
        'Butt Kicks',
        'Lateral Hops',
        'Tuck Jumps',
        'Bear Crawls',
    ],
    'forță': [
        'Push-up',
        'Pull-up',
        'Deadlift',
        'Bench Press',
        'Overhead Press',
        'Dumbbell Row',
        'Goblet Squat',
        'Romanian Deadlift',
        'Weighted Lunges',
        'Chest Dip',
        'Barbell Curl',
        'Hip Thrust',
    ],
    'definire': [
        'Biceps Curl',
        'Tricep Dip',
        'Lateral Raise',
        'Crunch',
        'Lunge',
        'Russian Twist',
        'Leg Raise',
        'Side Plank',
        'Cable Fly',
        'Reverse Crunch',
        'Cable Lateral Raise',
        'Glute Bridge',
    ],
    'rezistență': [
        'Jump Rope',
        'High Knees',
        'Rowing',
        'Cycling',
        'Box Jumps',
        'Step-Ups',
        'Medicine Ball Slams',
        'Battle Ropes',
        'Ski Erg',
        'Burpee Broad Jump',
        'Mountain Climber Sliders',
        'Jumping Lunges',
    ],
}

            mapping = {
                'începător':   (3, 12),
                'intermediar': (4, 10),
                'avansat':     (5, 8),
            }
            sets, reps = mapping.get(level, (4,10))
            pool = exercises.get(goal.lower(), [])
            chosen = random.sample(pool, min(4, len(pool)))

            ctx['plan'] = [
                {'name': ex, 'sets': sets, 'reps': reps}
                for ex in chosen
            ]
        return ctx





# class WorkoutPlanListView(LoginRequiredMixin, ListView):
#     model               = WorkoutPlan
#     template_name       = 'plan_list/plan_list.html'
#     context_object_name = 'plans'
#     paginate_by         = 10
#
#     def get_queryset(self):
#         return WorkoutPlan.objects.filter(user=self.request.user) \
#                                   .order_by('-created')

