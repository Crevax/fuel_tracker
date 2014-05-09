from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Sum, Avg, Max, Min
from fuel_tracker.models import FuelUp
from fuel_tracker.forms import FuelUpForm

def index(request):
    context = RequestContext(request)

    return render_to_response('fuel_tracker/fuel_up/index.html', {}, context)    

def detail(request):
    context = RequestContext(request)

@login_required
def add(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = FuelUpForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return HttpResponseRedirect(reverse('fuel_up.index'))
        else:
            print form.errors
    else:
        form = FuelUpForm()

    return render_to_response('fuel_tracker/fuel_up/add.html', {'form': form}, context)

@login_required
def edit(request):
    context = RequestContext(request)