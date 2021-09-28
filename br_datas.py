from datetime import datetime, timedelta
import locale


class DataBr:

    def __init__(self):
        self.__criado_em = datetime.today() - timedelta(days=3, hours=12)
        locale.setlocale(locale.LC_TIME, "pt_BR")

    def __repr__(self):
        return f"DataBr(criado_em='{self.criado_em.strftime('%d/%m/%Y %H:%M:%S')}')"

    def __str__(self):
        return self.data_formatada()

    @property
    def criado_em(self):
        return self.__criado_em

    def mes_cadastro(self):
        mes_cadastro = self.criado_em.strftime('%B').capitalize()
        return mes_cadastro

    def dia_da_semana(self):
        dia_da_semana = self.criado_em.strftime('%A').capitalize()
        return dia_da_semana

    def data_formatada(self):
        return self.criado_em.strftime('%d/%m/%Y %H:%M')

    def tempo_de_cadastro(self):
        return datetime.today() - self.criado_em

