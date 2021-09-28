from br_datas import DataBr

data_br = DataBr()
print(data_br)
datas = [data_br]
print(datas)
print(f"Mês: {data_br.mes_cadastro()}")
print(f"Dia da semana: {data_br.dia_da_semana()}")
print(f"Tempo de cadastro: {data_br.tempo_de_cadastro()}")
