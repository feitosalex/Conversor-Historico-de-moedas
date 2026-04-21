import streamlit as st
from main import buscar_moeda,historico
import pandas as pd

st.set_page_config(page_title='Finanças',layout='wide')

if 'origem' not in st.session_state:
    st.session_state.origem='BRL'
if 'destino' not in st.session_state:
    st.session_state.destino='USD'


Conversão, Histórico,Sumário = st.tabs(['🔄 Conversão de Valores', '📈 Histórico de Moedas','🌐 Sumário das moedas'])

with Conversão:
    st.header('🔄 Conversor de moedas')
    col1, col2= st.columns(2)
    with col1:
        moeda_base= st.selectbox('Moeda:',('BRL','USD','GBP','BTC','JPY','EUR','CAD','CHF','AUD','ARS','CLP','CNY'),
                                 key='origem',
                                 index=None,
                                 placeholder='Escolha a origem')
        

    with col2:
        moeda_destino= st.selectbox('Moeda:',('BRL','USD','GBP','BTC','JPY','EUR','CAD','CHF','AUD','ARS','CLP','CNY'),
                                    key='destino',
                                    index=None,
                                    placeholder='Escolha o destino')


    valor=st.number_input('Valor a ser convertido', min_value=0.0, step=1.0)
        
    if moeda_base and moeda_destino:
        if st.button('Converter valor'):
            if moeda_destino== 'BTC':
                paridade=buscar_moeda(f'{moeda_destino}-{moeda_base}')
                resultado= valor/paridade if paridade else 0
                st.metric(label=f'Valor em {moeda_base} convertido para {moeda_destino}',value=f'{resultado:.8f} em {moeda_destino}')
            else:
                paridade=buscar_moeda(f'{moeda_base}-{moeda_destino}')
                resultado= valor* paridade if paridade else 0
                st.metric(label=f'Valor em {moeda_base} convertido para {moeda_destino}',value=f'{resultado:.2f} em {moeda_destino}')
        else:
            st.info('Selecione as moedas de origem e destino')

with Histórico:
    st.header('📈 Variação Histórica')
    col1,col2=st.columns([1,3])
    with col1:
            moedas= st.multiselect('Escolha as moedas que deseja acessar o histórico:',['USD','GBP','BTC','JPY','EUR','CAD','CHF','AUD','ARS','CLP','CNY'])
            qtd_dias= st.number_input('Histórico de quantos dias deseja?',min_value=2,value=7)
    with col2:
        if moedas:
            data= {moeda:historico(moeda,qtd_dias) for moeda in moedas}
            df= pd.DataFrame(data)
            datas=pd.date_range(end=pd.Timestamp.now(), periods=qtd_dias, freq='D')
            df['Data']= datas.strftime('%d/%m/%Y')
            df_display= df.set_index('Data')
            st.line_chart(df_display, x_label='Data', y_label='Valor em R$')
            with st.expander(f'Histórico de {qtd_dias} dias'):
                st.dataframe(df_display.style.format('R${:.2f}'))
        else:
            st.warning('Selecione ao menos uma moeda (ex: USD)')
    
with Sumário:
    st.header("🌐 Guia de Moedas Disponíveis")
    st.markdown("Confira as moedas que você pode monitorar neste painel:")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🌎 South America")
        st.write(" **BRL**: Real Brasileiro")
        st.write(" **ARS**: Peso Argentino")
        st.write(" **CLP**: Peso Chileno")

    with col2:
        st.markdown("### 🌎 Europe")
        st.write(" **EUR**: Euro")
        st.write(" **GBP**: Libra Esterlina")
        st.write(" **CHF**: Franco Suíço")

    with col3:
        st.markdown("### 🌏 Asia")
        st.write(" **JPY**: Iene Japonês")
        st.write(" **CNY**: Yuan Chinês")

    st.divider()

    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("### 🌎 North America")
        st.write(" **USD**: Dólar Americano")
        st.write(" **CAD**: Dólar Canadense")

    with col5:
        st.markdown("### 🌍 Africa")
        st.write(" **ZAR**: Rand Sul-Africano")

    with col6:
        st.markdown("### 🌍 Oceania")
        st.write("**AUD**: Dólar Australiano")

    # Categoria Principal: Criptomoedas
    with st.expander("⚡ Ativos Digitais & Criptos", expanded=True):
        st.info("Cotações descentralizadas com atualização em tempo real.")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.write("🟠 **BTC**: Bitcoin")
        with c2:
            st.write("🔷 **ETH**: Ethereum")
        with c3:
            st.write("🪙 **LTC**: Litecoin")
            
    st.caption("Dados fornecidos pela AwesomeAPI • Atualizado via Streamlit")