from rest_framework import serializers


class CalculatorFinalScoresResponseSerializer(serializers.Serializer):
    technology_level = serializers.IntegerField()
    commercialization_level = serializers.IntegerField()
    technology_score = serializers.IntegerField()
    product_development = serializers.IntegerField()
    product_definition = serializers.IntegerField()
    competitive_landscape = serializers.IntegerField()
    team = serializers.IntegerField()
    go_to_market = serializers.IntegerField()
    supply_chain = serializers.IntegerField()
