import requests


def buscar_moeda(par:str):
    url=f' https://economia.awesomeapi.com.br/last/{par}'
    try:
        resposta= requests.get(url)
        if resposta.status_code ==200:
            resposta_json= resposta.json()
            moeda_chave= par.replace('-','')
            return float(resposta_json[moeda_chave]['bid'])
    except Exception as e:
        print(f'Erro na busca:{e}')
    return 0.0 

def historico(moeda:str, dias:int):
    par= f'{moeda}-BRL' if '-' not in moeda else moeda
    url=F' https://economia.awesomeapi.com.br/daily/{par}/{dias}'
    resposta= requests.get(url)
    if resposta.status_code ==200:
        historico= resposta.json()
        return [float(dia['bid']) for dia in historico][::-1]
    return [0.0]* dias
