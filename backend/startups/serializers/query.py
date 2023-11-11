from rest_framework import serializers


class ApplicantQuerySerializer(serializers.Serializer):
    is_qualified = serializers.BooleanField(required=False)
