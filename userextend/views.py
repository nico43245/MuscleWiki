
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import CreateView
import random
from userextend.forms import UserForm


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model= User
    form_class = UserForm
    success_url = '/login/'

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)  # OPRESC SALVAREA pentru a prelucra valorile din formular
            new_user.first_name = new_user.first_name.upper()  # modifica ca valoarea pentru first_name sa fie scrisa cu MAJUSCULA
            new_user.last_name = new_user.last_name.upper()
            numere=random.randint(100000,999999)
            new_user.username=f"{new_user.first_name[0].lower()}_{new_user.last_name.lower()}_{numere}"
            new_user.save()


        return super(UserCreateView,self).form_valid(form)

