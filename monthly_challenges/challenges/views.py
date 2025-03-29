from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthly_challenges ={
    "january" : "Eat Daily twice and run for 30 minutes",
    "february": "run for 1hr:30 minutes"
}

def monthly_challenegr_by_number(request, month):
   
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    forward_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + forward_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Month is not Found")
        
    