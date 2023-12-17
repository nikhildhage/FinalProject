import os

from django.shortcuts import render
from django.utils.dateparse import parse_date, parse_time
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

from .models import Reservation


# Create your views here.

def index(request):
    return render(request, "index.html")


def menu(request):
    return render(request, "menus.html")


# Locations view
def locations(request):
    return render(request, "locations.html")


# Reservations View
def reservations(request):
    #  # Extracting  form data from reservation form
    if request.method == 'POST':
        first_name = request.POST.get('FirstName')
        last_name = request.POST.get('LastName')
        email = request.POST.get('Email')
        phone_number = request.POST.get('PhoneNumber')
        arrival_date = parse_date(request.POST.get('ReservationDate'))
        arrival_time = parse_time(request.POST.get('ReservationTime'))
        comments = request.POST.get('myComments')

        # Create Reservation instance
        reservation = Reservation(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            arrival_date=arrival_date,
            arrival_time=arrival_time,
            comments=comments
        )
        reservation.save()  # Save the reservation to the database

        email_content = f"""
                <h1><strong>This is a Heading 1 with Bold Text</strong></h1><br><br>
                Here are your reservation details:<br><br>
                First Name: {first_name} <br><br>
                Last Name :{last_name} <br><br>
                Email: {email}<br><br>
                Phone Number: {phone_number}<br><br>
                Reservation Date: {arrival_date}<br><br>
                Reservation Time: {arrival_time}<br><br>
                Comments: {comments}
                """
        try:
            message = Mail(
                from_email='ndhage64.work@gmail.com',
                to_emails=email,
                subject='Restaurant Reservation Confirmation for ' + first_name + last_name,
                html_content=email_content)
            sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
    return render(request, "reservations.html")


# Activities View
def giftcards(request):
    return render(request, "giftCard.html")


# Details View
def contact(request):
    return render(request, "contact.html")
