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
    technology_score = 0
    product_development = 0
    product_definition = 0
    competitive_landscape = 0
    team = 0
    go_to_market = 0
    supply_chain = 0

    for answer in calculator_answers:
        question = answer.calculator_question
        category = answer.calculator_question.category.category.lower()

        if category == "technology":
            technology_score = question.score
        elif category == "product development":
            product_development = question.score
        elif category == "product definition/design":
            product_definition = question.score
        elif category == "competitive landscape":
            competitive_landscape = question.score
        elif category == "team":
            team = question.score
        elif category == "go-to-market":
            go_to_market = question.score
        elif category == "manufacturing/supply chain":
            supply_chain = question.score

    if technology_score >= 4:
        technology_level = 4
    if technology_score >= 5:
        technology_level = 5
    if product_development >= 2 and product_definition >= 3:
        technology_level = 6
    if product_development >= 3:
        technology_level = 7
    if product_development >= 4:
        technology_level = 8
    if product_development >= 5:
        technology_level = 9

    if competitive_landscape >= 1 and team >= 1:
        commercialization_level = 1
    if competitive_landscape >= 2 and team == 2:
        commercialization_level = 2
    if (
        product_development >= 1
        and product_definition >= 1
        and competitive_landscape >= 3
        and team >= 2
        and go_to_market >= 1
    ):
        commercialization_level = 3
    if (
        product_definition >= 2
        and competitive_landscape >= 4
        and team >= 2
        and go_to_market >= 2
        and supply_chain >= 1
    ):
        commercialization_level = 4
    if (
        product_definition >= 4
        and competitive_landscape >= 5
        and team >= 3
        and go_to_market >= 3
        and supply_chain >= 2
    ):
        commercialization_level = 5
    if product_definition >= 5 and team >= 4 and go_to_market >= 4:
        commercialization_level = 6
    if team >= 4 and supply_chain >= 3:
        commercialization_level = 7
    if team >= 5 and supply_chain >= 4:
        commercialization_level = 8
    if team >= 5 and supply_chain >= 5:
        commercialization_level = 9

    return (
        technology_level,
        commercialization_level,
        technology_score,
        product_development,
        product_definition,
        competitive_landscape,
        team,
        go_to_market,
        supply_chain,
    )
