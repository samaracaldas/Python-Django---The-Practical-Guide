from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse




monthly_challenges = {
    "january": "Eat no meat for the entire month!", 
    "february": "Walk at least 20 minutes  every day.",
    "march": "Learn Django for at least 20 minutes every day!", 
    "april": "Eat no meat for the entire month!",
    "may": "Walk at least 20 minutes  every day.",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk at least 20 minutes  every day.",
    "september": "Learn Django for at least 20",
    "october": "Eat no meat for the entire month!",
    "november" : "Walk at least 20 minutes  every day.",
    "december": None     
        
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months" : months
    })
        

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
            
        } )
    except:
        raise Http404()


