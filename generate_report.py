import os
import pandas as pd
import mysql.connector
from config import MYSQL_CONFIG, REPORTS_PATH
from datetime import datetime

def conectar_mysql():
    try:
        return mysql.connector.connect(**MYSQL_CONFIG)
    except mysql.connector.Error as err:
        print(f"Erro de conexão MySQL: {err}")
        raise

def gerar_relatorio():
    if not os.path.exists(REPORTS_PATH):
        os.makedirs(REPORTS_PATH)

    query_path = os.path.join('queries', 'monthly_report.sql')
    with open(query_path, 'r') as f:
        query = f.read()

    conn = conectar_mysql()
    df = pd.read_sql(query, conn)
    conn.close()

    # Gerar arquivo Excel com timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    arquivo_excel = os.path.join(REPORTS_PATH, f'relatorio_mensal_{timestamp}.xlsx')
    df.to_excel(arquivo_excel, index=False)

    print(f"Relatório gerado: {arquivo_excel}")

if __name__ == '__main__':
    gerar_relatorio()
