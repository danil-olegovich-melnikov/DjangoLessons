from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from . import utils
from .utils import check_car


@login_required
@check_car
def trip_list(request: HttpRequest, pk: int) -> HttpResponse:
    page = request.GET.get('page', 1)
    start_day = request.GET.get('start_day', "")
    end_day = request.GET.get('end_day', "")

    car = utils.car_get_by_pk(user=request.user, pk=pk)
    trips = utils.trip_get(pk=pk, start_day=start_day, end_day=end_day)
    n_pages = []

    if trips.num_pages > 1:
        n_pages = range(1, trips.num_pages + 1)

    return render(request, 'car/trips.html', context={
        "car": car,
        "trips": trips.page(page),
        "n_pages": n_pages,
        "start_day": start_day,
        "end_day": end_day,
    })


@login_required
@check_car
def trip_add(request: HttpRequest, pk: int) -> HttpResponseRedirect:
    if request.method == "POST":
        utils.trip_append(
            int(pk),
            int(request.POST.get("number_of_km", 0)),
            request.POST.get("date", ''),
        )
    return redirect(reverse('car:trip_list', args=[pk]))


@login_required
@check_car
def trip_delete(request: HttpRequest, pk: int, pk_trip: int) -> HttpResponseRedirect:
    utils.trip_delete(pk_trip)
    return redirect(reverse('car:trip_list', args=[pk]))
