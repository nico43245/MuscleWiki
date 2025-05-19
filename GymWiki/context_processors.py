from exercises.models import MuscleGroup

def all_muscle_groups(request):
    return {
        'muscle_groups': MuscleGroup.objects.all().order_by('name')
    }