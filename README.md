# Automação de Relatórios Mensais

Projeto em Python para extrair dados do MySQL e gerar relatórios mensais em Excel, reduzindo o tempo de entrega em 40%.

## Estrutura do projeto

- `generate_report.py` → Script principal para gerar o relatório
- `queries/monthly_report.sql` → Query SQL que extrai os dados do banco
- `reports/` → Pasta onde os relatórios Excel são salvos
- `config.py` → Configuração de conexão e variáveis de ambiente
- `.env.example` → Exemplo de arquivo para variáveis de ambiente
- `requirements.txt` → Dependências do projeto

## Como usar

1. Configure seu arquivo `.env` baseado no `.env.example`.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Coloque a query SQL na pasta `queries/` (já existe um exemplo).
4. Execute o script para gerar o relatório:
   ```bash
   python generate_report.py
   ```
5. Os relatórios gerados ficam na pasta `reports/`.

## Automação

Você pode agendar a execução do script diariamente ou mensalmente usando ferramentas como:
- Agendador de Tarefas do Windows
- Cron no Linux

## Licença

MIT License
