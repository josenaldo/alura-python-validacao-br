from validate_docbr import CPF, CNPJ


class Documento:
    @staticmethod
    def criar_novo(documento):
        doc_str = str(documento)

        tamanho_documento = len(doc_str)
        if tamanho_documento == 11:
            return DocCpf(doc_str)
        elif tamanho_documento == 14:
            return DocCnpj(doc_str)
        else:
            raise ValueError(f"Tamanho do documento ({tamanho_documento} dígitos) é inválido! ")


class DocCpf:
    def __init__(self, documento):
        if(self.valida(documento)):
            self.__valor = documento
        else:
            raise ValueError("CPF Inválido!")

    def __repr__(self):
        return self.formata()

    @staticmethod
    def valida(documento):
        validador = CPF()
        return validador.validate(documento)

    def formata(self):
        validador = CPF()
        return validador.mask(self.valor)

    @property
    def valor(self):
        return self.__valor


class DocCnpj:
    def __init__(self, documento):
        if (self.valida(documento)):
            self.__valor = documento
        else:
            raise ValueError("CNPJ Inválido!")

    def __repr__(self):
        return self.formata()

    @staticmethod
    def valida(documento):
        validador = CNPJ()
        return validador.validate(documento)

    def formata(self):
        validador = CNPJ()
        return validador.mask(self.valor)

    @property
    def valor(self):
        return self.__valor
