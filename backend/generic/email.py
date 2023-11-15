from django.core.mail import send_mail


def send_email(subject, message, recipient_list, *args, **kwargs):
    from_email = "launchlab90@gmail.com"
    try:
        send_mail(subject, message, from_email, recipient_list, html_message=message)
    except Exception as e:
        print(e)
