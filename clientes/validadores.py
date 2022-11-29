import re
from validate_docbr import CPF
def validar_cpf(numero_cpf):
    cpf=CPF()
    return cpf.validate(numero_cpf)
def validar_celular(numero_celular):
    """Verificando se o formato do celular 89 99410-1010"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return resposta