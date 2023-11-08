"""
Generic implementation for viewsets.
"""
from rest_framework import viewsets
from rest_framework.response import Response


class BaseViewSet(viewsets.GenericViewSet):
    def list_helper(self, request, *args, **kwargs):
        context = kwargs.get("context", self.get_serializer_context())
        queryset = kwargs.get("queryset", self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            serializer.context.update(context)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        serializer.context.update(context)
        return Response(serializer.data)  # pylint - disable=undefined-variable

    def retrieve_helper(self, request, *args, **kwargs):
        instance = self.get_object()
        context = kwargs.get("context", self.get_serializer_context())
        serializer = self.get_serializer(instance)

        serializer.context.update(context)
        return Response(serializer.data)
