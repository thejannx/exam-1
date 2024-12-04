from django.shortcuts import render
from .models import Taxi


def task_list(request):

    taxi_name = request.GET.get('taxi_name')
    license_plate = request.GET.get('license_plate')
    driver_name = request.GET.get('driver_name')
    passenger_capacity = request.GET.get('passenger_capacity')
    car_model = request.GET.get('car_model')
    is_completed = request.GET.get('is_completed')


    if taxi_name and license_plate and driver_name and passenger_capacity and car_model:
        try:
            Taxi.objects.create(
                taxi_name=taxi_name,
                license_plate=license_plate,
                driver_name=driver_name,
                passenger_capacity=int(passenger_capacity),
                car_model=car_model,
                is_completed=is_completed.lower() in ['true', '1', 'yes'],
            )
        except ValueError as e:

            print(f"Error creating Taxi: {e}")


    taxis = Taxi.objects.all()


    ctx = {'taxis': taxis}

    return render(request, 'taxi/task_list.html', ctx)
