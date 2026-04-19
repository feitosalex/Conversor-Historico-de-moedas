import streamlit as st
from main import buscar_moeda,historico
import pandas as pd

st.set_page_config(page_title='Finanças',layout='wide')

if 'origem' not in st.session_state:
    st.session_state.origem='BRL'
if 'destino' not in st.session_state:
    st.session_state.destino='USD'

Conversão, Histórico = st.tabs(['Conversão de Valores', 'Histórico de Moedas'])

with Conversão:
    st.title('Conversor de moedas')
    col1, col2= st.columns(2)
    with col1:
        moeda_base= st.selectbox('Moeda:',('BRL','USD','GBP','BTC','JPY','EUR'),
                                 key='origem',
                                 index=None,
                                 placeholder='Escolha a origem')
        

    with col2:
        moeda_destino= st.selectbox('Moeda:',('BRL','USD','GBP','BTC','JPY','EUR'),
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
    st.title ('Variação Histórica')
    col1,col2=st.columns([1,3])
    with col1:
            moedas= st.multiselect('Escolha as moedas que deseja acessar o histórico:',['USD','GBP','BTC','JPY','EUR'])
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
                st.dataframe(df_display.style.format('{:.2f}'))
        else:
            st.warning('Selecione ao menos uma moeda (ex: USD)')
        