from django.shortcuts import render, HttpResponse, redirect
from django.template.loader import render_to_string
from .forms import ContactForm
from django.core.mail import BadHeaderError, EmailMessage
from django.conf import settings
from honeypot.decorators import check_honeypot
from django.contrib import messages


def index(request):
    return render(request, 'home/index.html')


@check_honeypot(field_name='number')
def contact_form(request):
    """
    Send an email to the admin
    when site visitors send message
    via contact form and confirmation
    email to user, with copy of email.
    """
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            msg_contact = render_to_string('contact/contact(site_owner).txt',
                                           {'name': name,
                                            'email': form_email,
                                            'subject': subject,
                                            'message': message})
            msg_contact_confirm = render_to_string('contact/contact(user_confirmation).txt',
                                                   {'name': name,
                                                    'email': form_email,
                                                    'message': message})
            try:
                email = EmailMessage(
                f"Contact form submission; { name }",
                msg_contact,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL,],
                reply_to=[form_email],
                )
                email.send(fail_silently=False)
                email_confirm = EmailMessage(
                    "Contact Confirmation",
                    msg_contact_confirm,
                    settings.DEFAULT_FROM_EMAIL,
                    [form_email, ],
                )
                email_confirm.send(fail_silently=False)
                messages.success(request, 'Thank you for submitting '
                                 'the contact form!')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return redirect('contact_response')
    context = {
        'form': form,
    }
    return render(request, 'contact/contact_form.html', context)


def contact_response(request):
    """
    A view to render thank you page after site visitors send a contact form
    """
    return render(request, 'contact/contact_response.html')