from br_telefone import TelefoneBr


def cria_e_imprime_telefone(tipo_telefone, numero_telefone):
    try:
        telefone = TelefoneBr(numero_telefone)
        print(f"{tipo_telefone.capitalize()} com valor '{numero_telefone}' criado: {telefone}")
    except ValueError as error:
        print(f"Ocorreu um erro ao criar o {tipo_telefone} {numero_telefone}")
        print(f"\t{error}")
    print()


numeros_telefone = {
    "telefone_celular_valido": "5534912345678",
    "telefone_celular_sem_pais_valido": "34912345678",
    "telefone_fixo_valido": "453432345678",
    "telefone_fixo_sem_pais_valido": "3432345678",

    "telefone_com_caracteres_de_menos": "12345678",
    "telefone_com_caracteres_de_mais": "1234567812345678",
    "telefone_com_valor_invalido_de_ddd_que_comeca_com_zero": "5504912345678",
    "telefone_fixo_invalido_com_prefixo_iniciado_em_um": "453412345678",
}

for tipo, numero in numeros_telefone.items():
    cria_e_imprime_telefone(tipo, numero)
