from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Sum, Avg, Max, Min
from fuel_tracker.models import Vehicle, User, FuelUp
from fuel_tracker.forms import VehicleForm

def index(request):
    context = RequestContext(request)

    return render_to_response('fuel_tracker/vehicle/index.html', {}, context)

def detail(request, owner_name, vehicle_nickname):
    context = RequestContext(request)

    vehicle_nickname = vehicle_nickname.replace('_', ' ')

    context_dict = {'vehicle_nickname': vehicle_nickname}

    if request.user.username != owner_name:
        return HttpResponse('401: Unauthorized', status=401)

    try:
        owner = User.objects.get(username=owner_name)
        vehicle = Vehicle.objects.get(nickname=vehicle_nickname, owner=owner.id)

        fuel_ups = FuelUp.objects.filter(vehicle=vehicle).order_by('-date')[:5]

        gas_info = FuelUp.objects.filter(
                        vehicle = vehicle
                    ).aggregate(
                        #Sum('cost'),
                        Avg('price_per_gallon'),
                        Max('price_per_gallon'),
                        Min('price_per_gallon')
                    )

        miles = FuelUp.objects.filter(
                    vehicle = vehicle
                ).exclude(
                    miles_traveled = 0
                ).aggregate(
                    Sum('miles_traveled'),
                    Avg('miles_traveled'),
                    Max('miles_traveled'),
                    Min('miles_traveled')
                )

        context_dict['fuel_ups'] = fuel_ups
        context_dict['vehicle'] = vehicle
        context_dict['miles'] = miles
        context_dict['gas_info'] = gas_info
    except Vehicle.DoesNotExist:
        pass

    return render_to_response('fuel_tracker/vehicle/detail.html', context_dict, context)

@login_required
def add(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = VehicleForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return HttpResponseRedirect(reverse('main.index'))
        else:
            print form.errors
    else:
        form = VehicleForm()

    return render_to_response('fuel_tracker/vehicle/add.html', {'form': form}, context)

@login_required
def edit(request, owner_name, vehicle_nickname):
    context = RequestContext(request)