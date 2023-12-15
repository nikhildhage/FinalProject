import os

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.dateparse import parse_date
from sendgrid import SendGridAPIClient

from Restaurant.models import Reservation


# Create your views here.

def yurts(request):
    return render(request, "yurts.html")


# Activities View
def activities(request):
    return render(request, "activities.html")


# Reservations View
def reservations(request):

    if request.method == 'POST':
        # Extracting form data
        first_name = request.POST.get('myFName')
        last_name = request.POST.get('myLName')
        email = request.POST.get('myEmail')
        phone_number = request.POST.get('myPhone')
        arrival_date = parse_date(request.POST.get('myDate'))

        comments = request.POST.get('myComments')

        # Create Reservation instance
        reservation = Reservation(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            arrival_date=arrival_date,
            comments=comments
        )
        reservation.save()  # Save the reservation to the database

        # Create User instance and link it to the reservation
        user = User(
            user_firstname=first_name,
            user_lastname=last_name,
            user_email=email,
            reservation=reservation
        )
        user.save()  # Save the user to the database

        email_content = f"""
                <strong>Your reservation has been confirmed.</strong><br><br>
                Here are your reservation details:<br>
                Name: {first_name} {last_name}<br>
                Email: {email}<br>
                Phone: {phone_number}<br>
                Arrival Date: {arrival_date}<br>
                Nights: {nights}<br>
                Comments: {comments}
                """
        try:
            message = Mail(
                from_email='ndhage64.work@gmail.com',
                to_emails=email,
                subject='Pacific Trails Resort Reservation Confirmation for ' + first_name + last_name,
                html_content=email_content)
            sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)

        return redirect('details')

    return render(request, "reservations.html")


# Details View
def details(request):
    return render(request, "reservationDetails.html")
