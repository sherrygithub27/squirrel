from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from squirrel.models import squirrel
from .forms import SquirrelForm

def map(request):
    alldata = squirrel.objects.all()
    assignment = {"s_t":alldata}
    return render(request, 'squirrel/map.html', assignment)

def sightings(request):
    alldata = squirrel.objects.all()
    assignment = {"s_t":alldata}
    return render(request, 'squirrel/sightings.html', assignment)


def update(request,unique_squirrel_id):
    s_t = squirrel.objects.get(Unique_Squirrel_ID=unique_squirrel_id)
    if request.method == 'POST':
        #check form data
        form = SquirrelForm(request.POST, instance=s_t)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{Unique_Squirrel_ID}')
    else:
        form = SquirrelForm(instance=s_t)
    context = {
        'form':form,
    }
    return render(request, 'squirrel/update.html',context)

def add(request):
    if request.method == 'POST':
        #check form data
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SquirrelForm()
    context = {
        'form':form,
    }
    return render(request, 'squirrel/update.html',context)

def stats(request):
    total_counts = squirrel.objects.count()
    AM_counts = squirrel.objects.filter(Shift = 'AM').count()
    PM_counts = squirrel.objects.filter(Shift = 'PM').count()
    adult_counts = squirrel.objects.filter(Age = 'Adult').count()
    juvenile_counts = squirrel.objects.filter(Age = 'Juvenile').count()
    gray_counts = squirrel.objects.filter(Primary_Fur_Color = 'Gray').count()
    cinnamon_counts = squirrel.objects.filter(Primary_Fur_Color = 'Cinnamon').count()
    black_counts = squirrel.objects.filter(Primary_Fur_Color = 'Black').count()
    running_counts = squirrel.objects.filter(Running = True).count()
    chasing_counts = squirrel.objects.filter(Chasing = True).count()
    climbing_counts = squirrel.objects.filter(Climbing = True).count()
    eating_counts = squirrel.objects.filter(Eating = True).count()

    context = {
        'total_counts': total_counts,
	'AM_counts': AM_counts,
	'PM_counts': PM_counts,
	'adult_counts': adult_counts,
	'juvenile_counts': juvenile_counts,
	'gray_counts': gray_counts,
	'cinnamon_counts': cinnamon_counts,
	'black_counts': black_counts,
	'running_counts': running_counts,
	'chasing_counts': chasing_counts,
	'climbing_counts': climbing_counts,
	'eating_counts': eating_counts,
    }

    return render(request, 'squirrel/stats.html', context)

def main_page(request):
    return render(request, 'squirrel/home.html')
