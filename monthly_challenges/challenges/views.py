from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    redirect_path = reverse("month-challenge",args=[forward_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("Month is not Found")
        
    