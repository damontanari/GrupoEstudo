import pandas as pd
import numpy as np
import re

def convert_sql_to_cquery(query):
    CRLF = " + CRLF\n" 
    query = re.sub(r"BETWEEN '(.*?)' AND '(.*?)'", "BETWEEN ? AND ?", query)
    query = re.sub(r"IN \((.*?)\)", "IN (?)", query)
    query = re.sub(r"= '(.*?)'", "= ?", query)
    query = query.replace("SELECT", 'cQuery += "SELECT"').replace("\n", " + CRLF\n")
    query = query.replace("FROM", 'cQuery += "FROM"').replace("INNER JOIN", 'cQuery += "INNER JOIN"')
    query = query.replace("WHERE", 'cQuery += "WHERE"').replace("ORDER BY", 'cQuery += "ORDER BY"')
    query = query.replace("     ", "     ")  
    query = query.replace(" + CRLF\n + CRLF", " + CRLF") 
    query = query.replace(' + CRLF\n', '') + '"'
    return query

original_query = """
SELECT
    SB8.B8_FILIAL,
    SB8.B8_LOCAL,
    SB8.B8_PRODUTO,
    SB1.B1_DESC,
    SB1.B1_TIPO,
    SB8.B8_LOTECTL,
    SB8.B8_DTVALID,
    SB8.B8_SALDO
FROM SB8010 SB8
    INNER JOIN SB1010 SB1 ON SB1.B1_FILIAL = '90'
        AND SB1.B1_COD = SB8.B8_PRODUTO
        AND SB1.B1_TIPO IN ('PA', 'SP')
        AND D_E_L_E_T = ''
WHERE D_E_L_E_T = ''
    AND SB8.B8_FILIAL = '90'
    AND SB8.B8_PRODUTO BETWEEN '00001' AND '00010'
    AND SB8.B8_LOCAL BETWEEN '01' AND '03'
    AND SB8.B8_LOTECTL BETWEEN 'xxx' AND 'xxx'
    AND SB8.B8_DTVALID BETWEEN '20241101' AND '20241105'
ORDER BY SB8.B8_FILIAL, SB8.B8_PRODUTO, SB1.B1_TIPO, SB8.B8_LOTECTL
"""


query_vendas = """
SELECT 
    id,
    DATE(data_venda) AS data_venda,
    id_cliente,
    nome_cliente,
    id_vendedor,
    nome_vendedor,
    produto,
    categoria,
    quantidade,
    preco_unitario,
    valor_total,
    forma_pagamento,
    status,
    DATE(created_at) AS data_criacao,
    DATE(updated_at) AS data_att
FROM (
  SELECT
        v1.*,
        v2.nome AS nome_vendedor,
        c.nome AS nome_cliente
    FROM vendas v1
        -- Cruzando para trazer o nome do vendedor
        LEFT JOIN vendedores v2 ON v1.id_vendedor = v2.id_vendedor
        -- Cruzando para trazer o nome do cliente
        LEFT JOIN clientes c ON v1.id_cliente = c.id
        ) AS dfVendas;
"""
# Chama a função para converter para cQuery
cQuery_example = convert_sql_to_cquery(query_vendas)

# Exibe a query no formato cQuery +=
print(cQuery_example)






    

