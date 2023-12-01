from users import models as users_models
from generic.email import send_email
from generic import utils as generic_utils
from django.template.loader import render_to_string


def send_approval_email(email, **other_fields):
    password = generic_utils.generate_random_password()

    user = users_models.StartupUser.objects.create_user(
        email=email, password=password, **other_fields
    )

    mydic = {"email": email, "password": password}
    subject = "LaunchLab Application Approved – Welcome aboard!"
    html_template = "emailtemplate.html"
    message = render_to_string(html_template, context=mydic)
    recipient_list = [email]
    send_email(subject, message, recipient_list)

    return user


def send_rejection_email(email):
    subject = "LaunchLab Application Status"
    message = "Body of the email."
    recipient_list = [email]
    send_email(subject, message, recipient_list)
