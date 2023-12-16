import os

from django.shortcuts import render
from django.utils.dateparse import parse_date
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
        first_name = request.POST.get('myFName')
        last_name = request.POST.get('myLName')
        email = request.POST.get('myEmail')
        phone_number = request.POST.get('myPhone')
        arrival_date = parse_date(request.POST.get('myDate'))
        nights = request.POST.get('myPhone')
        comments = request.POST.get('myComments')

        # Create Reservation instance
        reservation = Reservation(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            arrival_date=arrival_date,
            nights=nights,
            comments=comments
        )
        reservation.save()  # Save the reservation to the database

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
    return render(request, "reservations.html")


# Activities View
def giftcards(request):
    return render(request, "giftCard.html")


# Details View
def contact(request):
    return render(request, "contact.html")
