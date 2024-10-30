
# Importando as bibliotecas necessárias para o projeto
import pandas as pd
from pandas.tseries.offsets import MonthEnd
import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import locale

# Pandas - Para trabalhar com dados (ETL)
# Datetime - Para trabalhar com variáveis de datas
# Locale - Para definir a linguagem do projeto se necessário

### Configurações e variáveis que costumo fazer antes de começar o projeto ###

# Definindo linguagem local PT-BR UTF-8
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') 

# Variáveis de datas para auxiliar no ETL
data = datetime.datetime.now() # Capturar a data atual
data -= datetime.timedelta(days=1) # Capturar data anterior

data_atual = datetime.datetime.now().strftime("%Y-%m-%d") # Formatando a data atual para (Ano-Mês-Dia)
data_anterior = data.strftime("%Y-%m-%d") # Formatando a data anterior para (Ano-Mês-Dia)

ultima_atualizacao = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Definindo data de atualização para controle de banco de dados

# Coletnado dia, mês e ano atual
dia = datetime.datetime.now().strftime("%d")
mes = datetime.datetime.now().strftime("%m")
ano = data.strftime("%Y")

nome_mes = f'{mes} - {datetime.datetime.now().strftime("%B")}' # %B Serve para coletar o nome do mes referenciado
print(nome_mes)

primeiro_dia_mes = f'{ano}-{mes}-01' # Travando uma data por exemplo sempre primeiro dia do mês

# Função para pegar sempre o último dia do mês
def ultimo_dia(mes, ano):
    data_inicial = datetime.datetime(ano, mes, 1)
    ultimo_dia_do_mes = data_inicial + relativedelta(months=1) - datetime.timedelta(days=1)
    return ultimo_dia_do_mes.strftime("%Y-%m-%d")
ultimo_dia(9,2024)
