from django.shortcuts import render, HttpResponse, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings


def contactform(request):
    """
    Send an email to the admin
    when site visitors send message via contact form
    """

    if request.POST:
        contact_form = request.POST(ContactForm)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(
                          f"You've got a message from {name}"
                          f"({email}) on contact form.",
                          f"Subject: {subject}, Message: {message}",
                          email,
                          [settings.DEFAULT_FROM_EMAIL],
                        )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return redirect('contact_response')
    return render(request, 'contact/contact_form.html')
    # else:
    # return


def contact_response(request):
    """
    A view to render thank you page after site visitors send a contact form
    """
    return render(request, 'home/contact_response.html')
