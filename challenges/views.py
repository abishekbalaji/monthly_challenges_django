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


def monthly_challenge_by_no(request, month):
    if month > len(monthly_challenges) or month <= 0:
        return HttpResponseNotFound('Invalid month')
    redirect_month = list(monthly_challenges.keys())[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_to=redirect_path)


def monthly_challenge(request, month):
    print("*********request: ", request,
          dir(request), request.body, request.path)
    challenge_text = monthly_challenges.get(month, None)
    if challenge_text:
        return HttpResponse(challenge_text)
    return HttpResponseNotFound(f'This month {month} is not supported.')
