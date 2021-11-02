from django.urls import path
from . import views  # . = same folder

urlpatterns = [
    path("", views.index), # executed for /challenges/
    path(("<int:month>"), views.monthly_challenge_by_number),
    # with the 'name'of this URL, we can use it to construct PATH URL pointing to this URL dynamically
    path(("<str:month>"), views.monthly_challenge, name="month-challenge"), # name = path to point at a URL




]
