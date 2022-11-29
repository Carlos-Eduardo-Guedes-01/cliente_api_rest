from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validador(self, data):
        if not validar_cpf(data['cpf']):
            raise serealizers.ValidationError({'cpf':"O cpf não é válido."})
        if not validar_celular(data['celular']):
            raise serealizers.ValidationError({'celular':"O celular não está no formato aceito pelo sistema. Ex. 89 99410-1010"})
        return data
    
    def validar_nome(self, nome):
        if not nome.isalpha():
            raise serealizers.ValidationError("Não inclua números neste campo")
        return nome 
    
    def validar_rg(self, rg):
        if(len(rg) != 9):
            raise serealizers.ValidationError("O rg deve ter 9 dígitos")
        return rg