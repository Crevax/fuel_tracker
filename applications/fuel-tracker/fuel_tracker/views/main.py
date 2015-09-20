from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Sum, Avg, Max, Min
from fuel_tracker.models import *
from fuel_tracker.forms import *

def index(request):
    # The context contains information such as the client's machine details
    context = RequestContext(request)

    if request.user.is_authenticated():
        # Construct a dictionary to pass to the template engine as its context.
        vehicle_list = Vehicle.objects.order_by('nickname')[:5]
        context_dict = {'vehicles': vehicle_list}
    else:
        context_dict = {}

    # Return a rendered response to send to the client.
    return render_to_response('fuel_tracker/index.html', context_dict, context)

def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response(
                'fuel_tracker/register.html',
                {
                    'user_form': user_form,
                    'profile_form': profile_form,
                    'registered': registered
                },
                context
            )

def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/fuel_tracker/')
            else:
                return HttpResponse("Your account is not enabled.")
        else:
            print "Invalid login detaisl: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('fuel_tracker/login.html', {}, context)

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/fuel_tracker/')