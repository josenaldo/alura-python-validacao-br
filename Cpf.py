class Cpf:
    def __init__(self, documento):
        documento = str(documento)

        if self.cpf_eh_valido(documento):
            self.__cpf = documento
        else:
            raise ValueError("CPF Inválido")

    @property
    def cpf(self):
        return self.__cpf

    def __str__(self):
        return self.formata_cpf()

    def formata_cpf(self):
        fatia1 = self.cpf[:3]
        fatia2 = self.cpf[3:6]
        fatia3 = self.cpf[6:9]
        fatia4 = self.cpf[9:]

        return f'{fatia1}.{fatia2}.{fatia3}-{fatia4}'


    def cpf_eh_valido(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False
