from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges ={
    "january" : "Eat Daily twice and run for 30 minutes",
    "february": "run for 1hr:30 minutes",
    "december": None
}


def index(request):
    
    
    month = list(monthly_challenges.keys())
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    
    #     list_items +=f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # response_data = f"<ul>{list_items}<ul/>"
    
    response_data = render(request, "challenges/index.html",{
        "months":month
    })
    
    return HttpResponse(response_data)
    

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
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        # raise Http404()
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
        
    