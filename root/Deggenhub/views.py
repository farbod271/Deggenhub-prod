from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm, EventForm, CustomSignupForm, ProfileForm
from .models import CustomUser, Task, Event
from .weather import get_weather
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render



def index(request):
    #get all task and event objects in order of creation and pass them to the template
    tasks = Task.objects.all().order_by('-created')
    events = Event.objects.all().order_by('-created')
    weather_updates = get_weather()   #context = {temperature, weather_description, humidity, wind_speed}
    context = {
        'tasks': tasks,
        'events': events,
        'weather_updates': weather_updates
    }
    return render(request, 'Deggenhub/index.html', context)


@login_required
def create_task(request):
    if request.method == 'POST':
        
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user  
            task.save()
            print('Task created')
            print(form.errors)
            return redirect('index')
    
    else:
        form = TaskForm()  
        return render(request, 'Deggenhub/create-task.html', {'form': form})

@login_required
def create_event(request):
    if request.user.is_authenticated:
     if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user
            event.save()
        return redirect('index')
     else:
        form = EventForm() 
        return render(request, 'Deggenhub/create-event.html', {'form': form})
    else:
        raise Http404('you are not authorized to create an event')
    
@login_required
def delete_event(request, pk):
    user = request.user
    event = get_object_or_404(Event, pk=pk) 
    
    if request.user.is_authenticated and event.owner == user :
        if request.method == 'POST':
            event.delete()
            return redirect('profile')
    else:
        raise Http404('you are not authorized to delete this event')
    
@login_required
def delete_task(request, pk):
    user = request.user
    task = get_object_or_404(Task, pk=pk) 
    
    if request.user.is_authenticated and task.owner == user :
        if request.method == 'POST':
            task.delete()
            return redirect('profile')
    else:
        raise Http404('you are not authorized to delete this event')

@login_required
def update_event(request, pk):
    user = request.user
    event = get_object_or_404(Event, pk=pk)
    form = EventForm(request.POST, request.FILES, instance=event)
    if user.is_authenticated and event.owner == user:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('profile')
            else:
                raise Http404('form is not valid')
        else:
            form = EventForm(instance=event)
            context = {'form': form, 'pk': pk, 'event': event}
            return render(request, 'Deggenhub/update-event.html', context)
    else:
        raise Http404('you are not authorized to update this event')
    
@login_required
def update_task(request, pk):
    user = request.user
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST, request.FILES, instance=task)
    if user.is_authenticated and task.owner == user:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('profile')
            else:
                raise Http404('form is not valid')
        else:
            form = TaskForm(instance=task)
            context = {'form': form, 'pk': pk, 'task': task}
            return render(request, 'Deggenhub/update-task.html', context)
    else:
        raise Http404('you are not authorized to update this task')


def signup(request):
        
        if request.user.is_authenticated:
            messages.error(request, 'You are already logged in')
            return redirect('index')
        

        form = CustomSignupForm()
        if request.method == 'POST':

            # if request.user.is_authenticated:
            #     return redirect('index')
            form = CustomSignupForm(request.POST, request.FILES)

            # user = get_user_model()
            if form.is_valid():
                user = form.save()
                # user.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'account/signup.html', {'form': form})
                            
        else:
            form = CustomSignupForm()    
            return render(request, 'account/signup.html', {'form': form})
        
        
@login_required
def profile(request):
    user = request.user
    form = ProfileForm(instance=user)
    events = Event.objects.filter(owner = user).order_by('-created')
    tasks = Task.objects.filter(owner = user).order_by('-created')

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        temp_user = form.data['username']
        temp_mail = form.data['email']

        if CustomUser.objects.filter(username=temp_user).exists() and not CustomUser.objects.filter(username=temp_user, id=user.id).exists():
                # print('Username already exists')
                messages.error(request, 'Username already exists')
                return redirect('profile')


        if CustomUser.objects.filter(email=temp_mail).exists() and not CustomUser.objects.filter(email=temp_mail, id=user.id).exists():
                messages.error(request, 'Email already exists')
                return redirect('profile')


        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {'events': events , 'tasks': tasks}
    return render(request, 'Deggenhub/profile.html', context)

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'Deggenhub/task-detail.html', {'task': task})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'Deggenhub/event-detail.html', {'event': event})

