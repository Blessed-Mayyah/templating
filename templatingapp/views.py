from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import TaskForm
from .models import Task
# Create your views here.
tasks = {'monday':'Attend Class', 'tuesday':'Have a meeting', 'Wednesday':'Go Shopping', 'Thursday':'Washing', 'Friday':'Juma Prayers', 'Saturday':'Chill with the Girls', 'Sunday':'Resting'}
def task(request):
    # to_do = tasks.get(day)
    form = TaskForm()
    return render(request, 'templatingapp/base.html', {'task':'to_do', 'title':'day', 'form':form})
    
def index(request):
    return HttpResponse('<h1>Hello Uganda!</h1>')

def create_task(request):
    print('creating')
    if request.method == 'POST':
        form = TaskForm(request.POST)
       
        if form.is_valid(): 
            print('created')
            task_name = form.cleaned_data['name']
            details = form.cleaned_data['details']
            no_people = form.cleaned_data['no_people']
            # date_created = form.cleaned_data['date_created']
            day_of_week = form.cleaned_data['day_of_week']
        # if no_people is None: 
        #     Task.objects.create(name=task_name, details=details, no_people=no_people, day_of_week=day_of_week) 
        #     return HttpResponseRedirect(reverse('task'))
        # else:
        #     form.add_error('no_people must be specified')

    else:
        # tasklist = []
        form = TaskForm()
    tasklist = Task.objects.all()
        # print(tasklist)
    return render(request, 'templatingapp/base.html', {'tasklist':tasklist, 'form':form})


def delete_task(request, task_id):
    tasks = Task.objects.filter(id=task_id).delete()
    redirect_url = reverse('create_task')
    return HttpResponseRedirect(redirect_url)

def update_task(request, task_id):
    tasks = Task.objects.get(id=task_id)#instead of filter-retrieves items-returns even the duplicates, u can use get-only returns the unique thing
    print(tasks)
    if request.method == 'POST':
        form = TaskForm(request.POST) 
        if form.is_valid(): 
            a_name = form.cleaned_data['name']  
            b_details = form.cleaned_data['details']
            c_no_of_people = form.cleaned_data['c_no_of_people']
            d_day_of_week = form.cleaned_data['d_day_of_week']
            
            #Updating fiels in the database
            tasks.name = a_name
            tasks.details = b_details
            tasks.no_people = c_no_of_people
            tasks.day_of_week = d_day_of_week
            tasks.save()
            redirect_url = reverse('create_task')
            return HttpResponseRedirect(redirect_url)
    else:
        form =TaskForm(initial={'name': tasks.name, 'details': tasks.details, 'no_of_people': tasks.no_of_people, 'day_of_week': tasks.day_of_week,})
        return render(request, 'templatingapp/update_task.html',{'form':form, 'task_id':task_id})
    
