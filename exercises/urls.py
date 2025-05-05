
from exercises import views
from django.urls import path

from home.views import HomeTemplateView




urlpatterns=[
    path('add_exercise',views.ExerciseCreateView.as_view(),name='exercise-add'),
    path('grupe/',views.MuscleGroupListView.as_view(),name='muscle-group-list'),

    path('exercise/<int:pk>/edit/',views.ExerciseUpdateView.as_view(),name='exercise-edit'),

    path('grupe/<slug:slug>/',views.ExerciseListView.as_view(),name='exercise-list'),


    path('exercise/<int:pk>/',views.ExerciseDetailView.as_view(),name='exercise-detail'),

    path('exercise/<int:pk>/delete/',views.ExerciseDeleteView.as_view(),name='exercise-delete'),
]