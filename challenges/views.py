from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    'january': 'Eat no meat for the month',
    'february': 'Walk atleast for 20 mins everyday',
    'march': 'Learn django for atleats 20 mins everyday',
    'april': 'Eat no meat for the month',
    'may': 'Walk atleast for 20 mins everyday',
    'june': 'Learn django for atleats 20 mins everyday',
    'july': 'Eat no meat for the month',
    'august': 'Walk atleast for 20 mins everyday',
    'september': 'Learn django for atleats 20 mins everyday',
    'october': 'Eat no meat for the month',
    'november': 'Walk atleast for 20 mins everyday',
    'december': 'Learn django for atleats 20 mins everyday'
}

# Create your views here.


def index(request):
    list_items = ""

    for month in monthly_challenges:
        month_path = reverse('month-challenge', args=[month])
        list_items += f'<li><a href="{month_path}">{month.capitalize()}</a></li>'

    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)


def monthly_challenge_by_no(request, month):
    if month > len(monthly_challenges) or month <= 0:
        return HttpResponseNotFound('<h1>Invalid month</h1>')
    redirect_month = list(monthly_challenges.keys())[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_to=redirect_path)


def monthly_challenge(request, month):
    print("*********request: ", request,
          dir(request), request.body, request.path)
    challenge_text = monthly_challenges.get(month, None)
    response_data = f'<h1>{challenge_text}</h1>'
    if challenge_text:
        return HttpResponse(response_data)
    return HttpResponseNotFound(f'<h1>This month {month} is not supported.</h1>')
