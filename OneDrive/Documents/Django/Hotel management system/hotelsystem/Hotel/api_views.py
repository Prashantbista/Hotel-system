from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets

from .models import Client
from.serializers import ClientSerializer
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class ClientViewSet(viewsets.ModelViewSet):
        queryset = Client.objects.all()
        serializer_class = ClientSerializer
        permission_classes= [IsAuthenticatedOrReadOnly]


        filter_backends = [
            DjangoFilterBackend,
            SearchFilter,
            OrderingFilter,
        ]

        filterset_fields = ["reservation_time", "phone_number"]
        search_fields = ["name", "email", "table"]
        ordering_fields = ["name", ""]
        ordering = ["id"]



# class ClientlistAPIView(generics.ListCreateAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer

# class ClientlistAPIView(APIView):
#     def get (self, request):
#         client=Client.objects.all()
#         serializer = ClientSerializer(client, many=True)

#         return Response(serializer.data)