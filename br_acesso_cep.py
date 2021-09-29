import requests


class BuscaEndereco:
    url_busca_cep = "https://viacep.com.br/ws/"
    tipo_resultado = "json"

    def __init__(self, cep):
        if BuscaEndereco.valida(cep):
            self.__cep = str(cep)
            self.__endereco = self.busca_cep()
        else:
            raise ValueError(f"O CEP fornecido ({cep}) é inválido!")

    def __repr__(self):
        return f"BuscaEndereco(cep={repr(self.cep)}, endereco={repr(self.endereco)})"

    def __str__(self):
        return self.formata()

    @staticmethod
    def valida(cep):
        return len(str(cep)) == 8

    @property
    def cep(self):
        return self.__cep

    @property
    def endereco(self):
        return self.__endereco

    def busca_cep(self):
        url = self.__get_url_de_pequisa_do_cep()
        r = requests.get(url)

        if(r.status_code == 200):
            resposta = r.json()

            if(resposta.get('erro', False) is True):
                raise ValueError(f"O CEP buscado ({self.cep}) não foi encontrado")

            return r.json()
        else:
            r.raise_for_status()

    def formata(self):
        resultado = ""

        resultado += self.__get_campo_do_endereco('logradouro', 'LOGRADOURO')
        resultado += self.__get_campo_do_endereco('bairro', 'BAIRRO')
        resultado += self.__get_campo_do_endereco('complemento', 'COMPLEMENTO')
        resultado += self.__get_campo_do_endereco('localidade', 'LOCALIDADE')
        resultado += self.__get_campo_do_endereco('uf', 'ESTADO')
        resultado += self.__get_campo_do_endereco('cep', 'CEP')

        return resultado

    def __get_campo_do_endereco(self, campo, nome_campo):
        valor = self.endereco.get(campo, '')
        return f"{nome_campo}: {valor}\n" if valor else ''

    def __get_url_de_pequisa_do_cep(self):
        return f"{BuscaEndereco.url_busca_cep}/{self.cep}/{BuscaEndereco.tipo_resultado}"
