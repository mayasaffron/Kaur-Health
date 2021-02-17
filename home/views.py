from django.shortcuts import render, HttpResponse, redirect
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError


def index(request):
    return render(request, 'home/index.html')


def contactform(request):
    """
    Send an email to the admin
    when site visitors send message via contact form
    """
    contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
        name = contact_form.cleaned_data['name']
        email = contact_form.cleaned_data['email']
        subject = contact_form.cleaned_data['subject']
        message = contact_form.cleaned_data['message']
        try:
            send_mail(
                f"You've got a message from {name} ({email}) on contact form.",
                f"Subject: {subject}, Message: {message}",
                email,
                [settings.DEFAULT_FROM_EMAIL],
            )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

    return redirect('thankyou_page')
