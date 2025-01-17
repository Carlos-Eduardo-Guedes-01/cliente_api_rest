from rest_framework import viewsets, filters #novo
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from django_filters.rest_framework import DjangoFilterBackend

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter] #novo
    ordering_fields = ['nome',] #ordenar por nome
    search_fields = ['nome', 'cpf']#buscar por nome e cpf
    filterset_fields = ['ativo']