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
    tech = dev = def_val = comp = team = market = chain = 0

    for answer in calculator_answers:
        question = answer.calculator_question
        category = answer.calculator_question.category.category.lower()
        print(question.score)
        if category == "technology":
            tech = question.score
        elif category == "product development":
            dev = question.score
        elif category == "product definition/design":
            def_val = question.score
        elif category == "competitive landscape":
            comp = question.score
        elif category == "team":
            team = question.score
        elif category == "go-to-market":
            market = question.score
        elif category == "manufacturing/supply chain":
            chain = question.score

    if tech >= 4:
        technology_level = 4
    if tech >= 5:
        technology_level = 5
    if dev >= 2 and def_val >= 3:
        technology_level = 6
    if dev >= 3:
        technology_level = 7
    if dev >= 4:
        technology_level = 8
    if dev >= 5:
        technology_level = 9

    if comp >= 1 and team >= 1:
        commercialization_level = 1
    if comp >= 2 and team == 2:
        commercialization_level = 2
    if dev >= 1 and def_val >= 1 and comp >= 3 and team >= 2 and market >= 1:
        commercialization_level = 3
    if def_val >= 2 and comp >= 4 and team >= 2 and market >= 2 and chain >= 1:
        commercialization_level = 4
    if def_val >= 4 and comp >= 5 and team >= 3 and market >= 3 and chain >= 2:
        commercialization_level = 5
    if def_val >= 5 and team >= 4 and market >= 4:
        commercialization_level = 6
    if team >= 4 and chain >= 3:
        commercialization_level = 7
    if team >= 5 and chain >= 4:
        commercialization_level = 8
    if team >= 5 and chain >= 5:
        commercialization_level = 9
    
    
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
