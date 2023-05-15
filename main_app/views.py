from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Race
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
# from .forms import ContactsForm, JobForm
import requests

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/job')
        else:
            error_message = 'invalid credentials - please try again'
    form = UserCreationForm()
    context = {'form': form, 'error': error_message}
    return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'base.html')

def get_races(request):
    all_races = {}
    if 'name' in request.GET:
        name = request.GET['name']
        url ='@.com' 
        response = requests.get(url)
        data = response.json()
        races = data['races']

        for i in races:
            race_data = Race(
                name = i['strMeal'],
                category = i['strCategory'],
                instructions = i['strInstructions'],
                region = i['strArea'],
                slug = i['idMeal'],
                image_url = i['strMealThumb']
            )
            race_data.save()
            all_meals = Race.objects.all().order_by('-id')

    return render (request, 'races.html', { "all_races": 
    all_races} )

