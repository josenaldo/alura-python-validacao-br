from documento import Documento


def cria_e_imprime_documento(tipo_documento, numero_documento):
    try:
        documento = Documento.criar_novo(numero_documento)
        print(f"{tipo_documento.capitalize()} com valor '{numero_documento}' criado: {documento}")
    except ValueError as error:
        print(f"Ocorreu um erro ao criar o {tipo_documento} {numero_documento}")
        print(f"\t{error}")
    print()


numeros = {
    'numero_de_cpf_valido': 85827877409,
    'numero_de_cpf_invalido': 85827877406,
    'numero_de_cpf_com_digitos_a_menos': 85827877,
    'numero_de_cpf_com_digitos_a_mais': 858278774098,

    'numero_de_cnpj_valido': 71599366000177,
    'numero_de_cnpj_invalido': 71599366000178,
    'numero_de_cnpj_com_digitos_a_menos': 7159936600017,
    'numero_de_cnpj_com_digitos_a_mais': 71599366000177676,
}

for tipo, numero in numeros.items():
    cria_e_imprime_documento(tipo, numero)




