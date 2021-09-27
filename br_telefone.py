import re


class TelefoneBr:

    padrao = "([0-9]{2,3})?([1-9]{2})((?:[2-8]|9[1-9])[0-9]{3})([0-9]{4})"

    def __init__(self, numero):
        telefone = str(numero)

        if(self.valida(telefone)):
            self.__valor = numero
        else:
            raise ValueError(f"O telefone informado ({numero} é inválido)")

    def __repr__(self):
        return self.formata()

    @staticmethod
    def valida(numero):
        padrao_compilado = re.compile(TelefoneBr.padrao)
        combina = re.fullmatch(padrao_compilado, numero)
        if(combina):
            return True
        else:
            return False

    def formata(self):
        padrao_compilado = re.compile(TelefoneBr.padrao)
        grupos = re.search(padrao_compilado, self.valor)

        ddi = f"+{grupos.group(1)}" if grupos.group(1) else "+55"
        ddd = grupos.group(2)
        prefixo = grupos.group(3)
        sufixo = grupos.group(4)

        return f"{ddi}({ddd}){prefixo}-{sufixo}"

    @property
    def valor (self):
        return self.__valor
