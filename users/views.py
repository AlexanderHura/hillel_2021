from django.contrib.auth import get_user_model
#from django.http.response import HttpResponse
from django.views.generic import ListView
User = get_user_model()

# def users(requests):
#     users = User.objects.all()
#     results = ", ".join([user.username for user in users])
#     return HttpResponse(results)




class UsersView(ListView):
    template_name = 'users/users.html'
    queryset = User.objects.all()