from users import models as users_models
from generic.email import send_email
from generic import utils as generic_utils
from django.template.loader import render_to_string
from startups import models as startups_models


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
    html_template = "rejectemailtemplate.html"
    message = render_to_string(html_template)
    recipient_list = [email]
    send_email(subject, message, recipient_list)


def calculate_levels(startup_id):
    calculator_answers = startups_models.CalculatorQuestionAnswer.objects.filter(
        startup_id=startup_id
    )

    technology_level = 1
    commercialization_level = 1
    tech = dev = def_val = comp = team = market = chain = 1

    for answer in calculator_answers:
        question = answer.calculator_question
        category = question.category.category.lower()

        if category == "technology":
            tech += answer.score
        elif category == "development":
            dev += answer.score
        elif category == "defense":
            def_val += answer.score
        elif category == "competition":
            comp += answer.score
        elif category == "team":
            team += answer.score
        elif category == "market":
            market += answer.score
        elif category == "supply chain":
            chain += answer.score

    if dev >= 2 and def_val >= 3:
        technology_level = 6
    if dev >= 3:
        technology_level = 7
    if dev >= 4:
        technology_level = 8
    if dev >= 5:
        technology_level = 9

    if comp == 1 and team == 1:
        commercialization_level = 1
    elif comp == 2 and team == 2:
        commercialization_level = 2

    return (
        technology_level,
        commercialization_level,
        tech,
        dev,
        def_val,
        comp,
        team,
        market,
        chain,
    )
