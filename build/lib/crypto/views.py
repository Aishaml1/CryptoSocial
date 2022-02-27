# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


class Home(LoginView):
    template_name = 'main/home.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'main/signup.html', context)


    # return HttpResponse('Hello world')
    # def home_view(request):
    # user = request.user
    # hello = 'Welcome'
    


    # context = {
    #     'user': user,
    #     'hello' : hello,
    # }
    # return render(request, 'main/home.html', context)