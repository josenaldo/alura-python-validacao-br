from validate_docbr import CPF

cpf = CPF()
cpfs = []

for num in range(0, 99999999999):
    cpf_com_zeros = f'{num:011}'
    if cpf.validate(cpf_com_zeros):
        cpfs.append(cpf_com_zeros)

    if num % 10000 == 0 and num != 0:
        print('.', end='')
    if num % 1000000 == 0:
        print()

meu_cpf = '82094403572'
if meu_cpf in cpfs:
    cpf_formatado = cpf.mask(meu_cpf)
    print(f'{cpf_formatado} encontrado na lista')
else:
    print('CPF não encontrado')

print(f'Total de CPFs válidos encontrados: {len(cpfs):,}')

