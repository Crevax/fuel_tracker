from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Sum, Avg, Max, Min
from fuel_tracker.models import GasStation
from fuel_tracker.forms import GasStationForm

def index(request):
    context = RequestContext(request)

    return render_to_response('fuel_tracker/gas_station/index.html', {}, context)

def detail(request):
    context = RequestContext(request)

@login_required
def add(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = GasStationForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return HttpResponseRedirect(reverse('main.index'))
        else:
            print form.errors
    else:
        form = GasStationForm()

    return render_to_response('fuel_tracker/gas_station/add.html', {'form': form}, context)

def edit(request):
    context = RequestContext(request) 