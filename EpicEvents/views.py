from django.http import Http404
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from account.serializers import AccountSerializer
from account.models import Account
from contract.models import Contract
from contract.serializers import ContractSerializer
from event.models import Event
from event.serializers import EventSerializer


class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = AccountSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = []

    def get_object(self):
        lookup_field = self.kwargs["id"]
        return get_object_or_404(Account, id=lookup_field)


class ContractListCreateView(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = []

    def get_account(self):
        lookup_field = self.kwargs["id"]
        return get_object_or_404(Account, id=lookup_field)

    def get(self, request, *args, **kwargs):
        lookup_field = self.kwargs["id"]
        queryset = self.get_queryset().filter(account_id=lookup_field)
        serializer = ContractSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        lookup_field = self.kwargs["id"]
        serializer = ContractSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(account_id=lookup_field)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContractRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContractSerializer
    permission_classes = []
    queryset = Contract.objects.all()

    def get_account(self):
        lookup_field = self.kwargs["id"]
        return get_object_or_404(Account, id=lookup_field)

    def get_object(self):
        lookup_field = self.kwargs["id"]
        lookup_field2 = self.kwargs["contract_id"]

        try:
            return Contract.objects.get(account_id=lookup_field, id=lookup_field2)
        except Contract.DoesNotExist:
            raise Http404


class EventCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        lookup_field = self.kwargs["contract_id"]
        queryset = self.get_queryset().filter(contract_id=lookup_field)
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        lookup_field = self.kwargs["contract_id"]
        serializer = EventSerializer(data=request.data)
        if self.get_queryset().filter(contract_id=lookup_field).exists():
            return Response(data="Un évenement lié à ce contrat existe déjà", status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save(contract_id=lookup_field)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = []

    def get_object(self):
        lookup_field = self.kwargs["contract_id"]
        return get_object_or_404(Event, contract_id=lookup_field)