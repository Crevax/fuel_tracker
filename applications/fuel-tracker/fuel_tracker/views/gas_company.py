from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Sum, Avg, Max, Min
from fuel_tracker.models import GasCompany
from fuel_tracker.forms import GasCompanyForm

def index(request):
    context = RequestContext(request)

    return render_to_response('fuel_tracker/gas_company/index.html', {}, context)

def detail(request):
    context = RequestContext(request)

@login_required
def add(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = GasCompanyForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return HttpResponseRedirect(reverse('gas_company.index'))
        else:
            print form.errors
    else:
        form = GasCompanyForm()

    return render_to_response('fuel_tracker/gas_company/add.html', {'form': form}, context)

def edit(request):
    context = RequestContext(request)