import os

from django.shortcuts import render
from django.utils.dateparse import parse_date, parse_time
from python_http_client import UnauthorizedError
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

from .models import Reservation


def index(request):
    return render(request, "index.html")


def menu(request):
    return render(request, "menus.html")


# Locations view
def locations(request):
    return render(request, "locations.html")


# Reservations View
def reservations(request):
    # Capture  form data from reservation form
    if request.method == 'POST':
        first_name = request.POST.get('FirstName')
        last_name = request.POST.get('LastName')
        email = request.POST.get('Email')
        phone_number = request.POST.get('PhoneNumber')
        arrival_date = parse_date(request.POST.get('ReservationDate'))
        arrival_time = parse_time(request.POST.get('ReservationTime'))
        comments = request.POST.get('textArea')

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

        # Save the Reservation instance  to database
        reservation.save()

        # Reservation Conformation Email Template
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
        # Checking APi Key
        """ !import only for debuting purpose.
            !important disable when in production mode.
            Do not publicly share API_KEY
        """
        print("Check API KEY")
        print("----------------------------------------")
        sendgrid_api_key = os.environ.get('SENDGRID_API_KEY')
        print(f'SendGrid API Key: {sendgrid_api_key}')
        print("----------------------------------------\n")

        # Try sending email to SendGrid Maid Send Endpoint
        try:
            message = Mail(
                from_email='ndhage64.work@gmail.com',
                to_emails=email,
                subject='Restaurant Reservation Confirmation for ' + first_name + last_name,
                html_content=email_content)
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)

            # Getting Response BOdy
            print("")
            print(f'RESPONSE')
            print('-' * 15)
            print(response.status_code)
            print(response.body)
            print(response.headers)
            print('-\n' * 15)
        except UnauthorizedError as e:
            # Handling UnauthorizedError Exceptions
            print(f'ERROR: Unauthorized Error:{e.status_code}')
            print("----------------------------------------")
            print(f'UnauthorizedError: {e.status_code} - {e.body}')
            print("----------------------------------------\n")
        except Exception as e:
            # Handling Exceptions
            print("Other Exceptions")
            print("----------------------------------------")
            print(f'ERROR: {str(e)}')
            print(f'----------------------------------------')
    return render(request, "reservations.html")


# GiftCards View
def giftcards(request):
    return render(request, "giftCard.html")


# Contact View
def contact(request):
    return render(request, "contact.html")
