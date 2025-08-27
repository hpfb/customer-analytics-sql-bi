-- Clientes 

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Segmento VARCHAR(50),
    Regiao VARCHAR(50),
    DataContrato DATE,
    Plano VARCHAR(20) -- Enterprise, Pro e Basic.
);

-- Assinaturas (MRR)
CREATE TABLE Subscriptions (
    SubscriptionID INT PRIMARY KEY,
    CustomerID INT,
    DataInicio DATE,
    DataFim DATE,
    MRR DECIMAL(10, 2),
    Status VARCHAR(20), -- Ativo, Cancelado e Suspenso.
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Pesquisas
CREATE TABLE Surveys (
    SurveyID INT PRIMARY KEY,
    CustomerID INT,
    DataPesquisa DATE,
    Tipo VARCHAR(10), -- NPS, CSAT, CES e etc.
    Score INT, -- Escala de 1 a 10
    Comentarios TEXT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Pagamentos
CREATE TABLE Payments (
    PaymentID INT PRIMARY KEY,
    CustomerID INT,
    DataPagamento DATE,
    Valor DECIMAL(10, 2),
    StatusPagamento VARCHAR(20), -- Pago, Pendente e Falhado.
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);