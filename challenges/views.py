from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Something for january",
    "february": "Something for february"
}


def index(request):

    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        # generate a new link with a dynamic path for all months
        list_items += f"<li><a href=\"{month_path}\"> {capitalized_month} </a></li>" 
        # we get a long string with <li>...</li><li>...</li> ...

    # use triple quotes for a multi-line string
    response_data = f"<ul>{list_items}></ul>"

    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(challenges.keys())
    try:
        our_month = months[month-1]

        # reverse() alone points only to /challenge
        # args[] = the dynamic segment we have in the urls.py file, which is <int:month> => now we have /challenges/[month] configured
        # this builds a full path to the URL from urls.py with this name
        redirect_path = reverse("month-challenge", args=[our_month])

        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("Month not found in the database!")


def monthly_challenge(request, month):

    try:
        challenge_text = challenges[month] 
        # to output the html code inside the template, we fetch the file and transform its content into a string
        response_data = render_to_string("challenges/challenge.html")

    except:
        return HttpResponseNotFound("Month not found in the database!")

    return HttpResponse(challenge_text)
