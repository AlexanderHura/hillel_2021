from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
#from django.http.response import HttpResponse
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin

from .forms import CustomUserCreationForm



User = get_user_model()

# def users(requests):
#     users = User.objects.all()
#     results = ", ".join([user.username for user in users])
#     return HttpResponse(results)




class UsersView(PermissionRequiredMixin, ListView):
    permission_required = 'core.users'
    template_name = 'users/users.html'
    queryset = User.objects.all()

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    # Set user Group on registration
    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            # One user Group
            user_group = Group.objects.get(name=form.cleaned_data['groups'])
            user.groups.add(user_group)

            # Multiple user Groups
            # for form_ug in form.cleaned_data['groups']:
            #     user_group = Group.objects.get(name=form_ug.name)
            #     user.groups.add(user_group)

            # logout previouse user
            logout(request)

            # Authenticate and login user after registration
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)

            return redirect('home')
        else:
            return render(request, self.template_name, {'form' : form })


class LoginView(LoginView):
    template_name = 'registration/login.html'

    # Redirect from login page in case user already authenticated and loggedin
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return self.render_to_response(self.get_context_data())

