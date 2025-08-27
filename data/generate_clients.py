import random
from datetime import datetime, timedelta
from faker import Faker

# -------------------- Configurações --------------------
num_clients = 100
segments = ['SaaS', 'Saúde', 'Educação', 'Varejo', 'Financeiro', 'Alimentício', 'Tecnologia']
regions = ['Sudeste', 'Sul', 'Nordeste', 'Centro-Oeste', 'Norte']
plans = ['Basic', 'Pro', 'Enterprise']
survey_types = ['NPS', 'CSAT', 'CES']
payment_status = ['Pago', 'Pendente', 'Falhado']

fake = Faker('pt_BR')

# -------------------- Função para datas aleatórias --------------------
def random_date(start_year=2023, end_year=2025):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    return (start + timedelta(days=random.randint(0, (end-start).days))).date()

# -------------------- Preparar INSERTs --------------------
sql_text = ""

# -------------------- Customers --------------------
values_customers = []
for i in range(1, num_clients + 1):
    nome = fake.company().replace("'", "''")  # Escapa aspas simples
    segmento = random.choice(segments)
    regiao = random.choice(regions)
    data_contrato = random_date()
    plano = random.choice(plans)
    values_customers.append(f"({i}, '{nome}', '{segmento}', '{regiao}', '{data_contrato}', '{plano}')")

sql_text += "-- Customers\n"
sql_text += "INSERT INTO Customers (CustomerID, Nome, Segmento, Regiao, DataContrato, Plano) VALUES\n"
sql_text += ",\n".join(values_customers) + ";\n\n"

# -------------------- Subscriptions --------------------
values_subs = []
for i in range(1, num_clients + 1):
    subscription_id = 100 + i
    data_inicio = random_date(2024, 2024)
    data_fim = "NULL" if random.random() > 0.2 else f"'{random_date(2025, 2025)}'"
    plano = random.choice(plans)
    mrr = 500 if plano == 'Basic' else 1500 if plano == 'Pro' else random.choice([5000, 7000, 8000])
    status = 'Ativo' if data_fim == "NULL" else random.choice(['Cancelado', 'Suspenso'])
    values_subs.append(f"({subscription_id}, {i}, '{data_inicio}', {data_fim}, {mrr}, '{status}')")

sql_text += "-- Subscriptions\n"
sql_text += "INSERT INTO Subscriptions (SubscriptionID, CustomerID, DataInicio, DataFim, MRR, Status) VALUES\n"
sql_text += ",\n".join(values_subs) + ";\n\n"

# -------------------- Surveys --------------------
values_surveys = []
for i in range(1, num_clients + 1):
    survey_id = 200 + i
    data_pesquisa = random_date(2025, 2025)
    tipo = random.choice(survey_types)
    score = random.randint(1, 10)
    comentarios = "Satisfatório" if score >= 7 else "Pode melhorar"
    values_surveys.append(f"({survey_id}, {i}, '{data_pesquisa}', '{tipo}', {score}, '{comentarios}')")

sql_text += "-- Surveys\n"
sql_text += "INSERT INTO Surveys (SurveyID, CustomerID, DataPesquisa, Tipo, Score, Comentarios) VALUES\n"
sql_text += ",\n".join(values_surveys) + ";\n\n"

# -------------------- Payments --------------------
values_payments = []
for i in range(1, num_clients + 1):
    payment_id = 300 + i
    data_pagamento = random_date(2025, 2025)
    plano = random.choice(plans)
    valor = 500 if plano == 'Basic' else 1500 if plano == 'Pro' else random.choice([5000, 7000, 8000])
    status = random.choice(payment_status)
    values_payments.append(f"({payment_id}, {i}, '{data_pagamento}', {valor}, '{status}')")

sql_text += "-- Payments\n"
sql_text += "INSERT INTO Payments (PaymentID, CustomerID, DataPagamento, Valor, StatusPagamento) VALUES\n"
sql_text += ",\n".join(values_payments) + ";\n\n"

# -------------------- Salvar arquivo UTF-8 --------------------
with open("insert_data.sql", "w", encoding="utf-8") as f:
    f.write(sql_text)