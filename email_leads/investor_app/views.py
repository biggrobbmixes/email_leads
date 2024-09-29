from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse

def submit_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        email = request.POST['email']
        notes = request.POST['notes']

        # Construct the email message
        subject = 'New Investor Form Submission'
        message = f'Name: {name}\nAddress: {address}\nInvestor Email: {email}\nNotes: {notes}'

        # Send email to the specified addresses
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            ['arash@arashkhosroabadi.com', 'millennialconsultingservices@gmail.com'],
            fail_silently=False,
        )

        return HttpResponse('Form submitted successfully and email sent!')

    return render(request, 'form_page.html')
