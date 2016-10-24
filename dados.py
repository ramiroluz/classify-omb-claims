import urllib
import pandas as pd
from json import loads
from datetime import datetime
from datetime import timedelta
from datetime import timezone

meses = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

traduz_tipos = {
    'sugestapso': 'Sugestão',
    'solicitaassapso': 'Solicitação',
    'daovida': 'Dúvida',
    'reclamaassapso': 'Reclamação',
    'denaoncia': 'Denúncia',
    'elogio': 'Elogio',
    'pedido-de-acesso-a-informaassapso': 'Pedido de acesso à informação',
}

traduz_estados = {
    'accepted': 'Aceito',
    'pending': 'Pendente',
    'rejected': 'Rejeitada',
    'resolved': 'Resolvida',
    'moving': 'Tramitando',
}

def iso_string_to_datetime(string_date):
    return datetime.strptime(string_date.replace(':', ''), '%Y-%m-%dT%H%M%S%z')


def load_json_data(filename):
    if filename.startswith('http'):
        json_data = urllib.request.urlopen(filename).read().decode('utf-8')
    else:
        with open(filename) as json_file:
            json_data = json_file.read()
    claims_json = loads(json_data)
    claims = sorted(claims_json['claims'], key=lambda x:x['uri'])
    return claims


def to_month_name(some_date):
    return '{:02d} - {}'.format(some_date.month, meses[some_date.month])


def to_mes_ano(some_date):
    return '{}/{}'.format(meses[some_date.month][:3], some_date.year)


def titulo_do_tipo(tipo):
    return traduz_tipos[tipo]


def titulo_do_estado(estado):
    return traduz_estados[estado]


def prepara_dados(arquivo='http://www.ouvidoria.curitiba.pr.leg.br/@@ombudsman-json'):
    claims = load_json_data(arquivo)
    # return normaliza_dados(claims)
    return claims


def normaliza_dados(claims):
    dados = pd.io.json.json_normalize(claims)
    dados['creation_date'] = localiza(dados['creation_date'])
    dados['mes'] = dados['creation_date'].apply(to_month_name)
    dados['mesano'] = dados['creation_date'].apply(to_mes_ano)
    dados['tipo'] = dados['kind'].apply(titulo_do_tipo)
    dados['estado'] = dados['review_state'].apply(titulo_do_estado)
    return dados


def localiza(creation_date):
    creation_date = creation_date.astype('datetime64')
    creation_date = creation_date.dt.tz_localize('UTC')
    creation_date = creation_date.dt.tz_convert('America/Sao_Paulo')
    return creation_date

