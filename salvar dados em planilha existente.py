import pandas as pd
from datetime import datetime

# Nome do arquivo da planilha Excel
excel_file = 'dados_diarios.xlsx'

# Data atual
data_atual = datetime.today().strftime('%Y-%m-%d')

# Realize o cálculo diário (substitua esta parte com o seu próprio código)
valor_calculado = 42

# Verifique se o arquivo da planilha Excel já existe
try:
    df = pd.read_excel(excel_file)
except FileNotFoundError:
    # Se o arquivo não existe, crie um novo DataFrame
    df = pd.DataFrame(columns=['Data', 'Valor Calculado'])

# Crie um novo DataFrame com os dados calculados
novo_dado = {'Data': data_atual, 'Valor Calculado': valor_calculado}
novo_df = pd.DataFrame([novo_dado])

# Concatene o novo DataFrame com o DataFrame existente
df = pd.concat([df, novo_df], ignore_index=True)

# Salve o DataFrame atualizado na planilha Excel
df.to_excel(excel_file, index=False)
