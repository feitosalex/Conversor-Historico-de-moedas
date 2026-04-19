💹 Conversor e Histórico de Moedas
Uma interface financeira moderna construída com Python e Streamlit que permite realizar conversões diretas e acompanhar a variação histórica de moedas em tempo real.

🚀 Funcionalidades
Conversão em Tempo Real: Converte valores entre as principais moedas (BRL, USD, EUR, GBP, JPY, BTC) utilizando dados atualizados da AwesomeAPI.

Visualização Histórica: Gráficos interativos que mostram a variação das moedas nos últimos dias (configurável pelo usuário).

Análise de Dados: Tabela detalhada com os valores históricos arredondados e organizados por data.

Interface Wide: Layout expandido para melhor visualização dos gráficos e métricas.

🛠️ Tecnologias Utilizadas
Python - Linguagem base.

Streamlit - Para a criação da interface web.

Pandas - Para manipulação e tratamento dos dados.

AwesomeAPI - Fonte de dados das cotações.

📦 Como instalar e rodar
Clone o repositório:

Bash
git clone https://github.com/feitosalex/Conversor-Historico-de-moedas.git
cd Conversor-Historico-de-moedas
Crie um ambiente virtual (opcional, mas recomendado):

Bash
python -m venv venv
# No Windows:
venv\Scripts\activate
Instale as dependências:

Bash
pip install -r requirements.txt
Execute a aplicação:

Bash
streamlit run app.py
📝 Detalhes Técnicos
O projeto utiliza o padrão de Migrations conceituais para organização do histórico e fatiamento de listas em Python ([::-1]) para garantir que a ordem cronológica dos dados da API esteja correta no gráfico.