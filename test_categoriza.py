#!/usr/bin/env python3

import unittest
import rake
import dados
from categoriza import categoriza_claim

def helper_test(categ, protocolo, claims):
    url_tmpl = 'http://www.ouvidoria.curitiba.pr.leg.br/{}'
    claim_url_tmpl = url_tmpl.format('ouvidoria/{}')
    uri = claim_url_tmpl.format(protocolo)
    df = [claim for claim in claims if claim['uri'] == uri]
    claim = categoriza_claim(categ, df[0])
    return [item[0] for item in claim['keywords']]


class TestCategoriza(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        stoplist='stoplists/ouvidoria.txt'
        url_tmpl = 'http://www.ouvidoria.curitiba.pr.leg.br/{}'
        cls._categ = rake.Rake(stoplist)
        cls._claims = dados.prepara_dados()
        cls._claim_url_tmpl = url_tmpl.format('ouvidoria/{}')

    def test_20160620100241(self):
        expected = [
            'transparência',
            'prefeitura',
            'prefeitura contratou',
            'guardas municipais'
        ]

        value = helper_test(self._categ, '20160620100241', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150618134915(self):
        expected = [
            '156',
            'administração municipal',
            'central 156',
            'gestão municipal',
            'gestão',
            'ouvidoria',
            'protocolo',
            'resposta',
            'respostas',
            'serviço público',
            'transparência',
            'área',
        ]

        value = helper_test(self._categ, '20150618134915', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150520160850(self):
        expected = [
            'lixo',
            'coleta',
            'rua',
        ]

        value = helper_test(self._categ, '20150520160850', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150804104915(self):
        expected = [
            'asfalto',
            'buraco',
            'criação',
            'drenagem',
            'erosão',
            'galeria',
            'meio',
            'protocolo',
            'trânsito',
            'unidade',
            'águas pluviais',
            'árvores',
        ]

        value = helper_test(self._categ, '20150804104915', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150618123604(self):
        expected = [
            '156',
            'central 156',
            'comupa',
            'ouvidoria',
            'resposta',
            'respostas',
            'sgm',
        ]

        value = helper_test(self._categ, '20150618123604', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150526123609(self):
        expected = [
            '156',
            'animais',
            'atendimento prefeitura',
            'cães',
            'linha',
            'moradores',
            'ouvidoria',
            'prefeitura',
            'protocolo',
            'resposta',
            'rua',
        ]

        value = helper_test(self._categ, '20150526123609', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150803112423(self):
        expected = [
            'central 156',
            '156',
            'falta',
            'fiscalização',
            'trânsito',
            'setran',
            'agentes',
        ]

        value = helper_test(self._categ, '20150803112423', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160329214149(self):
        expected = [
            'ouvidoria',
            '156',
            'prefeitura',
        ]

        value = helper_test(self._categ, '20160329214149', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160421193732(self):
        expected = [
            'corte',
            'praça',
            'protocolo',
            'árvores',
            'moradores',
            '156',
            'prefeitura',
        ]

        value = helper_test(self._categ, '20160421193732', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160506144258(self):
        expected = [
            'agente setran',
            'agente',
            'agentes',
            'falta',
            'mal',
            'multado',
            'ouvidoria',
            'respostas',
            'setran',
        ]

        value = helper_test(self._categ, '20160506144258', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151215152445(self):
        expected = [
            'atendimento setran',
            'central 156',
            'falta',
            'fiscalização',
            'fiscalizações',
            'ouvidor',
            'setran',
            'transito',
        ]

        value = helper_test(self._categ, '20151215152445', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150521091041(self):
        expected = [
            '156',
        ]

        value = helper_test(self._categ, '20150521091041', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160212145358(self):
        expected = [
            'administração',
            'calçada',
            'coleta',
            'construção',
            'entulho',
            'protocolo',
            'recolhimento',
            'retiraram',
            'serviço',
        ]

        value = helper_test(self._categ, '20160212145358', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160401151335(self):
        expected = [
            'central 156',
            'demora',
            'iluminação pública',
            'lâmpada',
            'protocolo',
            'saúde',
            'troca',
            'unidade',
        ]

        value = helper_test(self._categ, '20160401151335', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150624113733(self):
        expected = [
            'roçada',
            'mato',
            '156', 
        ]

        value = helper_test(self._categ, '20150624113733', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150624152440(self):
        expected = [
            'sigiloso',
        ]

        value = helper_test(self._categ, '20150624152440', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150820090506(self):
        expected = [
            'calçada',
            'criação',
            'drenagem',
            'obra',
            'prefeitura',
            'protocolo',
            'pública',
            'recuperação',
            'resposta',
            'tubulação',
            'unidade',
            'via',
        ]

        value = helper_test(self._categ, '20150820090506', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160509103626(self):
        expected = [
            'iluminação pública',
            'manutenção',
            'luminária',
            'protocolo central 156',
        ]

        value = helper_test(self._categ, '20160509103626', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160310105617(self):
        expected = [
            'iluminação pública',
            'lâmpada queimada',
            'protocolo central 156',
            'troca',
        ]

        value = helper_test(self._categ, '20160310105617', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160310113232(self):
        expected = [
            'coleta',
            'lixo vegetal',
            'protocolo central 156',
            'retirada',
        ]

        value = helper_test(self._categ, '20160310113232', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160310110313(self):
        expected = [
            'coleta',
            'lixo vegetal',
            'protocolo central 156',
        ]

        value = helper_test(self._categ, '20160310110313', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160310113601(self):
        expected = [
            'iluminação pública',
            'lâmpada queimada',
            'protocolo central 156',
            'troca',
        ]

        value = helper_test(self._categ, '20160310113601', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160118170430(self):
        expected = [
            'atendida',
            'ouvidoria',
            'protocolo',
            'urbs',
        ]

        value = helper_test(self._categ, '20160118170430', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150812163908(self):
        expected = [
            'central 156',
            'lâmpadas',
            'manutenção',
            'protocolo',
            'troca',
        ]

        value = helper_test(self._categ, '20150812163908', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160411093742(self):
        expected = [
            'iluminação pública',
            'lâmpada queimada',
            'protocolo central 156',
            'troca',
        ]

        value = helper_test(self._categ, '20160411093742', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150910112005(self):
        expected = [
            'criação',
            'falta',
            'iluminação pública',
            'luminária',
            'luminárias',
            'lâmpada queimada',
            'lâmpada',
            'manutenção',
            'meio',
            'protocolo',
            'troca',
            'unidade',
        ]

        value = helper_test(self._categ, '20150910112005', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151210152843(self):
        expected = [
            'central 156',
            'demora',
            'iluminação pública',
            'lâmpada',
            'protocolo',
        ]

        value = helper_test(self._categ, '20151210152843', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160518104449(self):
        expected = [
            'iluminação pública',
            'lâmpada queimada',
            'protocolo central 156',
            'troca',
        ]

        value = helper_test(self._categ, '20160518104449', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150819113029(self):
        expected = [
            'central 156',
            'iluminação pública',
            'lâmpadas',
            'rua',
            'troca',
        ]

        value = helper_test(self._categ, '20150819113029', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160330112500(self):
        expected = [
            'atendimento',
            'central 156',
            'cohab',
            'demora',
            'menores',
            'moradia popular',
            'prefeitura',
            'protocolo',
        ]

        value = helper_test(self._categ, '20160330112500', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151001100204(self):
        expected = [
            '156',
            'atendida',
            'calçada',
            'coleta',
            'informação',
            'lixo orgânico',
            'lixo',
            'muita',
            'prefeitura',
            'protocolo 156',
            'retirada',
            'rua',
            'serviço',
        ]

        value = helper_test(self._categ, '20151001100204', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160125155421(self):
        expected = [
            'alvará',
            'atividades',
            'barulho',
            'bebidas alcoólicas',
            'bebidas',
            'fiscalização',
            'idade',
            'menores',
            'prefeitura',
            'protocolo',
            'rua residencial',
            'rua',
            'transito',
        ]

        value = helper_test(self._categ, '20160125155421', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160408155145(self):
        expected = [
            'atendimento',
            'central 156',
            'demora',
            'iluminação pública',
            'protocolo',
        ]

        value = helper_test(self._categ, '20160408155145', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150804104531(self):
        expected = [
            'atendimento',
            'coleta',
            'criação',
            'jardim',
            'lixo vegetal',
            'protocolo',
            'resíduos vegetais',
            'via',
        ]

        value = helper_test(self._categ, '20150804104531', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160309115607(self):
        expected = [
            'iluminação pública',
            'lâmpadas queimadas',
            'protocolo central 156',
            'publicidade',
            'troca',
        ]

        value = helper_test(self._categ, '20160309115607', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160601103836(self):
        expected = [
            'atraso',
            'atrasos',
            'gentileza',
            'linha',
            'motorista',
        ]

        value = helper_test(self._categ, '20160601103836', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160414180251(self):
        expected = [
            'atendimento',
            'demora',
            'protocolo',
            'serviço',
            'moradores',
            'prefeitura',
            'tapa buracos',
            'rua',
            'linhas',
            'ônibus',
            'buracos',
            'calçada',
            'central 156',
            'ouvidoria',
        ]

        value = helper_test(self._categ, '20160414180251', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151125100053(self):
        expected = [
            'corte',
            'árvore',
            'central 156',
            'prefeitura',
            'toco',
        ]

        value = helper_test(self._categ, '20151125100053', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160125150017(self):
        expected = [
            'coleta',
            'lixo vegetal',
            'central 156',
        ]

        value = helper_test(self._categ, '20160125150017', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160104134549(self):
        expected = [
            'atendida',
            'central 156',
            'denúncia',
            'iluminação pública',
            'lâmpadas queimadas',
            'lâmpadas',
            'meio',
            'muita',
            'ouvidoria',
            'praça',
            'protocolo',
            'público',
            'resposta',
            'terceira',
            'troca',
        ]

        value = helper_test(self._categ, '20160104134549', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160223085948(self):
        expected = [
            'dengue',
            'focos',
            'lixo',
            'mato',
            'pendente',
        ]

        value = helper_test(self._categ, '20160223085948', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151029152659(self):
        expected = [
            '156',
            'calçada',
            'lixo',
            'mato',
            'ouvidor',
            'praça',
            'protocolo',
            'rua',
            'terreno baldio',
            'terreno',
        ]

        value = helper_test(self._categ, '20151029152659', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160428090858(self):
        expected = [
            'corte',
            'prefeitura',
            'via pública',
            'árvore',
            'árvores',
        ]

        value = helper_test(self._categ, '20160428090858', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150702084208(self):
        expected = [
            'esporte',
            'esportes',
            'lazer',
            'playgrond',
            'populares',
            'rua',
            'ruas',
            'terreno',
            'área',
        ]

        value = helper_test(self._categ, '20150702084208', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160216115822(self):
        expected = [
            '156',
            'caixa',
            'captação',
            'falta',
            'orientação',
            'público',
            'relocação',
            'resposta',
        ]

        value = helper_test(self._categ, '20160216115822', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151222182926(self):
        expected = [
            'administração',
            'falta',
            'iluminação pública',
            'iluminação',
            'lâmpada queimada',
            'lâmpada',
            'protocolo',
            'rua',
        ]

        value = helper_test(self._categ, '20151222182926', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160329214149(self):
        expected = [
            '156',
            'ouvidoria',
            'prefeitura',
            'público',
            'serviço 156',
            'via 156',
        ]

        value = helper_test(self._categ, '20160329214149', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160409210448(self):
        expected = [
            'agendamento',
            'alcoólica',
            'hospital',
            'saúde',
            'unidade básica',
        ]

        value = helper_test(self._categ, '20160409210448', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160304160527(self):
        expected = [
            'central 156',
            'demora',
            'dengue',
            'fiscalização',
            'limpeza',
            'mosquito',
            'posto',
            'protocolo',
            'terreno público',
        ]

        value = helper_test(self._categ, '20160304160527', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160125150017(self):
        expected = [
            'atendida',
            'central 156',
            'coleta',
            'demora',
            'lixo vegetal',
            'protocolo',
            'serviço',
        ]

        value = helper_test(self._categ, '20160125150017', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160506110208(self):
        expected = [
            'operação tapa buraco',
            'buracos',
            'pavimentação',
            'rua',
            'central 156',
            'protocolo',
        ]

        value = helper_test(self._categ, '20160506110208', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160219085801(self):
        expected = [
            'atendimento',
            'boleto',
            'boletos',
            'central',
            'demora',
            'multa',
            'operação',
            'ordem',
            'pagamento',
            'praça',
            'prefeitura',
            'resposta',
            'trabalho',
        ]

        value = helper_test(self._categ, '20160219085801', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160426102814(self):
        expected = [
            'coleta',
            'lixo vegetal',
            'protocolo central 156',
        ]

        value = helper_test(self._categ, '20160426102814', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151016082403(self):
        expected = [
            '156',
            'fiscalização',
            'protocolo 156',
            'protocolo',
        ]

        value = helper_test(self._categ, '20151016082403', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160321094229(self):
        expected = [
            'caixa',
            'captação',
            'desobstrução',
            'limpeza',
            'protocolo central 156',
        ]

        value = helper_test(self._categ, '20160321094229', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150521092645(self):
        expected = [
            'asfalto',
            'buracos',
            'manutenção',
            'rua',
            'transito',
            'veículos',
        ]

        value = helper_test(self._categ, '20150521092645', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150602154107(self):
        expected = [
            'atendeu mal',
            'mal atendimento',
            'pública',
        ]

        value = helper_test(self._categ, '20150602154107', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160616091324(self):
        expected = [
            'protocolo central 156',
            'coleta',
            'lixo vegetal',
        ]

        value = helper_test(self._categ, '20160616091324', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150813173235(self):
        expected = [
            'central 156',
            'galhos',
            'poda',
            'público',
            'resposta',
            'rua',
            'árvore',
        ]

        value = helper_test(self._categ, '20150813173235', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160311140658(self):
        expected = [
            'caliça',
            'central 156',
            'coleta',
            'demora',
            'dengue',
            'mosquito',
            'protocolo',
            'recolhimento',
        ]

        value = helper_test(self._categ, '20160311140658', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160509191342(self):
        expected = [
            '156',
            'atendida',
            'coleta',
            'galhos',
            'árvore',
            'protocolo',
        ]

        value = helper_test(self._categ, '20160509191342', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150914142238(self):
        expected = [
            'coleta',
            'lixo vegetal',
            '156',
            'jardim',
            'criação',
            'protocolo',
            'resíduos',
            'resíduos vegetais',
            'unidade',
        ]

        value = helper_test(self._categ, '20150914142238', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150521085108(self):
        expected = [
            'bebida alcoólica',
            'bebidas',
            'estádios',
            'lei',
            'futebol',
            'vereadores',
        ]

        value = helper_test(self._categ, '20150521085108', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160413113805(self):
        expected = [
            'falta',
            'medicamento',
            'protocolo central 156',
        ]

        value = helper_test(self._categ, '20160413113805', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150818150225(self):
        expected = [
            'buraco',
            'calçada',
            'central 156',
            'fiscalização',
            'municipal',
            'operação tapa',
            'prefeitura',
            'rua',
            'ruas',
            'terreno',
        ]

        value = helper_test(self._categ, '20150818150225', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150713103429(self):
        expected = [
            'atendimento',
            'central 156',
            'iluminação pública',
            'protocolo',
            'rua',
            'via',
        ]

        value = helper_test(self._categ, '20150713103429', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160203142823(self):
        expected = [
            '156',
            'atendida',
            'iluminação pública',
            'lâmpada',
            'troca',
        ]

        value = helper_test(self._categ, '20160203142823', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160503110255(self):
        expected = [
            'drenagem',
            'rio',
            'central 156',
            'limpeza',
            'rua',
            'jardim',
            'retirada',
            'tronco',
            'protocolo',
        ]

        value = helper_test(self._categ, '20160503110255', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151120105605(self):
        expected = [
            'central 156',
            'fechamento',
            'via',
            'moradores',
            'preservação',
            'protocolo',
            'rua',
            'área',
        ]

        value = helper_test(self._categ, '20151120105605', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160503100006(self):
        expected = [
            'atendida',
            'atendimento',
            'cartão',
            'feira',
            'funcionário público',
            'orientação',
            'posto',
            'público',
            'saúde',
            'serviço público',
            'trabalho',
            'ubs',
            'vacina',
            'vacinação',
            'áreas',
        ]

        value = helper_test(self._categ, '20160503100006', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160318153937(self):
        expected = [
            'atendimento',
            'central 156',
            'iluminação pública',
            'iluminação',
            'protocolo',
        ]

        value = helper_test(self._categ, '20160318153937', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150803112423(self):
        expected = [
            '156',
            'agentes',
            'atendimento',
            'central 156',
            'falta',
            'fiscalização',
            'ouvidor',
            'resposta',
            'setran',
            'trânsito',
        ]

        value = helper_test(self._categ, '20150803112423', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150526123726(self):
        expected = [
            '156',
            'falta',
            'ouvidoria',
            'respostas',
            'via central 156',
        ]

        value = helper_test(self._categ, '20150526123726', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160318152111(self):
        expected = [
            'atendimento',
            'central 156',
            'coleta',
            'demora',
            'galhos',
            'protocolo',
        ]

        value = helper_test(self._categ, '20160318152111', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160113145621(self):
        expected = [
            'caliça',
            'central 156',
            'demora',
            'protocolo',
            'recolhimento',
            'rua',
            'serviço',
        ]

        value = helper_test(self._categ, '20160113145621', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160404101649(self):
        expected = [
            'poda',
            'protocolo central 156',
            'via pública',
            'árvore',
            'árvores',
        ]

        value = helper_test(self._categ, '20160404101649', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160128121251(self):
        expected = [
            '156',
            'informação',
            'iptu',
            'meio ambiente',
            'prefeitura',
            'preservação',
            'protocolo',
            'resposta',
            'via',
            'área',
        ]

        value = helper_test(self._categ, '20160128121251', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150911133111(self):
        expected = [
            'criação',
            'iluminação pública',
            'luminária',
            'luminárias',
            'lâmpada queimada',
            'lâmpada',
            'manutenção',
            'moradores',
            'protocolo',
            'troca',
            'unidade',
        ]

        value = helper_test(self._categ, '20150911133111', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160412094703(self):
        expected = [
            'coleta',
            'lixo vegetal',
            'protocolo central 156',
        ]

        value = helper_test(self._categ, '20160412094703', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150721163536(self):
        expected = [
            'iluminação pública',
            'jardim',
            'luminárias',
            'lâmpada queimada',
            'lâmpada',
            'manutenção',
            'meio',
            'protocolo',
            'rua',
            'troca',
            'unidade',
        ]

        value = helper_test(self._categ, '20150721163536', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150728145753(self):
        expected = [
            'iluminação pública',
            'jardim',
            'luminária',
            'luminárias',
            'lâmpada',
            'manutenção',
            'meio',
            'protocolo',
            'resposta',
            'rua',
            'troca',
            'unidade',
        ]

        value = helper_test(self._categ, '20150728145753', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151226191455(self):
        expected = [
            '156',
            'demora',
            'denúncia',
            'ouvidoria',
            'protocolo',
            'resposta',
        ]

        value = helper_test(self._categ, '20151226191455', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151001100255(self):
        expected = [
            'atendimento',
            'iluminação pública',
            'luminária',
            'lâmpada',
            'manutenção',
            'protocolo',
            'queimada',
            'rua',
        ]

        value = helper_test(self._categ, '20151001100255', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160218162110(self):
        expected = [
            'caixa',
            'captação',
            'limpeza',
            'protocolo 156',
            'resposta',
        ]

        value = helper_test(self._categ, '20160218162110', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151006103225(self):
        expected = [
            'central 156',
            'cohab',
            'construção',
            'denúncia',
            'fiscalização',
            'informação',
            'linha',
            'lixo',
            'moradores',
            'rua',
            'ruas',
            'serviço',
            'terreno',
            'área pública',
            'área',
        ]

        value = helper_test(self._categ, '20151006103225', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160415104050(self):
        expected = [
            'iluminação pública',
            'lâmpada queimada',
            'protocolo central 156',
            'troca',
        ]

        value = helper_test(self._categ, '20160415104050', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160419165612(self):
        expected = [
            'central 156',
            'atendimento',
            'demora',
            'iluminação demora',
            'protocolo'
        ]

        value = helper_test(self._categ, '20160419165612', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160505085053(self):
        expected = [
            'buracos',
            'falta',
            'fechamento',
            'operação tapa buracos',
            'pavimentação',
            'rua',
            'serviço',
            'trabalho',
        ]

        value = helper_test(self._categ, '20160505085053', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150805151335(self):
        expected = [
            'poda',
            'protocolo',
            'árvore',
            'árvores',
        ]

        value = helper_test(self._categ, '20150805151335', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150819104316(self):
        expected = [
            'atendida',
            'criação',
            'iluminação pública',
            'luminárias',
            'lâmpada queimada',
            'lâmpada',
            'manutenção',
            'meio',
            'protocolo',
            'troca',
            'unidade',
        ]

        value = helper_test(self._categ, '20150819104316', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160530155012(self):
        expected = [
            'atividades',
            'lei',
            'lei lei',
            'ouvidor',
            'relatório',
            'relatório circunstanciado',
            'ouvidoria municipal',
        ]

        value = helper_test(self._categ, '20160530155012', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160516094519(self):
        expected = [
            'fiscalização',
            'obras',
            'obra',
            'alvará',
            'construção',
            'protocolo central 156',
        ]

        value = helper_test(self._categ, '20160516094519', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160603110306(self):
        expected = [
            'iluminação pública',
            'central 156',
            'protocolo',
            'serviço',
        ]

        value = helper_test(self._categ, '20160603110306', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150817155325(self):
        expected = [
            'criação',
            'deficientes',
            'implantação',
            'protocolo',
            'rio',
            'unidade',
            'vagas',
        ]

        value = helper_test(self._categ, '20150817155325', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150720085945(self):
        expected = [
            'atendimento',
            'coleta',
            'jardim',
            'lixo vegetal',
            'meio',
            'protocolo',
            'resíduos vegetais',
            'unidade',
        ]

        value = helper_test(self._categ, '20150720085945', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150917104714(self):
        expected = [
            'atendimento',
            'coleta',
            'criação',
            'jardim',
            'lixo vegetal',
            'protocolo',
            'resíduos vegetais',
            'rua',
            'unidade',
        ]

        value = helper_test(self._categ, '20150917104714', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151111083243(self):
        expected = [
            '156',
            'mal',
            'municipais',
            'ouvidoria municipal',
            'ouvidoria',
            'protocolo 156',
            'protocolo',
            'resposta',
        ]

        value = helper_test(self._categ, '20151111083243', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160602150135(self):
        expected = [
            'falta',
            'iluminação pública',
            'iluminação',
        ]

        value = helper_test(self._categ, '20160602150135', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160506151735(self):
        expected = [
            '156',
            'alvara',
            'criação',
            'fiscalizacao',
            'fiscalizaçao',
            'fiscalização',
            'irregular',
            'lei',
            'meio',
            'placas',
            'prefeitura',
            'protocolo',
            'publicidade irregular',
            'publicidade',
            'recolhimento',
            'resposta',
            'retirada',
            'rua',
            'sigilosa',
            'via pública',
        ]

        value = helper_test(self._categ, '20160506151735', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150720110750(self):
        expected = [
            'iluminação',
            'implantação',
            'luminária',
            'meio',
            'moradores',
            'praça',
            'protocolo',
            'unidade',
        ]

        value = helper_test(self._categ, '20150720110750', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151204145848(self):
        expected = [
            'atendimento',
            'iluminação pública',
            'lâmpada',
            'protocolo 156',
            'rua',
            'serviço',
            'troca',
        ]

        value = helper_test(self._categ, '20151204145848', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150522105759(self):
        expected = [
            'lei',
            'lei municipal',
            'logradouros públicos',
            'abandono',
            'veículos',
        ]

        value = helper_test(self._categ, '20150522105759', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151016112813(self):
        expected = [
            'exemplar',
            'meio',
            'motorista',
            'praça',
            'ônibus',
        ]

        value = helper_test(self._categ, '20151016112813', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150520134542(self):
        expected = [
            'cortes',
            'via',
            'áreas verdes',
            'árvores',
        ]

        value = helper_test(self._categ, '20150520134542', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150521081032(self):
        expected = [
            'ouvidoria',
            '156',
        ]

        value = helper_test(self._categ, '20150521081032', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150521085957(self):
        expected = [
            '156',
        ]

        value = helper_test(self._categ, '20150521085957', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150521090454(self):
        expected = [
            '156',
            '156 via',
            'atendida',
            'serviço',
        ]

        value = helper_test(self._categ, '20150521090454', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150521091041(self):
        expected = [
            '156',
        ]

        value = helper_test(self._categ, '20150521091041', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150521091537(self):
        expected = [
            'funcionario',
            'posto',
            'saude',
        ]

        value = helper_test(self._categ, '20150521091537', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150521091952(self):
        expected = [
            'aula',
            'aulas',
            'ouvidoria',
        ]

        value = helper_test(self._categ, '20150521091952', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150618095403(self):
        expected = [
            'calçadas',
            'lei',
            'lixeiras irregulares',
            'lixeiras',
        ]

        value = helper_test(self._categ, '20150618095403', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150624152440(self):
        expected = [
            'sigiloso',
            'orientação',
        ]

        value = helper_test(self._categ, '20150624152440', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150624152928(self):
        expected = [
            'orientação',
        ]

        value = helper_test(self._categ, '20150624152928', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150720132602(self):
        expected = [
            'feira',
            'largo',
            'ordem',
        ]

        value = helper_test(self._categ, '20150720132602', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150720165320(self):
        expected = [
            'cartão transporte',
            'cartão',
            'lei',
            'recarga',
            'trabalho',
            'transporte',
            'urbs',
        ]

        value = helper_test(self._categ, '20150720165320', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150721094934(self):
        expected = [
            'atividades',
            'falta',
            'idoso',
            'medicamentos',
            'medicações',
            'postos',
            'saúde',
        ]

        value = helper_test(self._categ, '20150721094934', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150805151819(self):
        expected = [
            'esgoto',
            'smma',
        ]

        value = helper_test(self._categ, '20150805151819', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150805153014(self):
        expected = [
            'atividades',
            'aulas',
            'cidadania',
            'ginástica',
            'rua',
            'smelj',
            'suspensão',
            'terceira idade',
        ]

        value = helper_test(self._categ, '20150805153014', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150805190247(self):
        expected = [
            'ouvidor',
            'ouvidoria',
            'protocolo',
            'resposta',
        ]

        value = helper_test(self._categ, '20150805190247', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150824151751(self):
        expected = [
            'revestimento asfáltico',
            'rua',
            'ruas',
        ]

        value = helper_test(self._categ, '20150824151751', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150825143854(self):
        expected = [
            'criação',
            'animais',
            'zona residencial',
        ]

        value = helper_test(self._categ, '20150825143854', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150827172206(self):
        expected = [
            'cartão transporte',
            'cartão',
            'idade',
            'renovação',
            'transporte',
            'urbs',
        ]

        value = helper_test(self._categ, '20150827172206', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150830031023(self):
        expected = [
            'academia',
            'central 156',
            'implantação',
            'licença',
            'praça',
            'protocolo',
            'resposta'
        ]

        value = helper_test(self._categ, '20150830031023', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151007145751(self):
        expected = [
            'resposta',
            'denúncia',
        ]

        value = helper_test(self._categ, '20151007145751', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151007145802(self):
        expected = [
            'resposta',
            'denúncia',
        ]

        value = helper_test(self._categ, '20151007145802', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151007145805(self):
        expected = [
            'resposta',
            'denúncia',
        ]

        value = helper_test(self._categ, '20151007145805', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151007195233(self):
        expected = [
            'atendimento',
            'caixa',
            'iluminação pública',
            'resposta',
            'respostas',
        ]

        value = helper_test(self._categ, '20151007195233', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151211160022(self):
        expected = [
            'desobstrução',
            'bueiro',
        ]

        value = helper_test(self._categ, '20151211160022', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151212123927(self):
        expected = [
            'bloqueios',
            'fechamentos',
            'pedreira',
            'pública',
            'ruas',
            'terceira',
        ]

        value = helper_test(self._categ, '20151212123927', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151215223622(self):
        expected = [
            'berçário',
            'cemei',
            'cemeis',
            'cmei',
            'creche',
            'deixa',
            'lei',
            'licença',
            'prefeitura',
        ]

        value = helper_test(self._categ, '20151215223622', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151215224404(self):
        expected = [
            'berçário',
            'cemei',
            'cemeis',
            'cmei',
            'creche',
            'deixa',
            'lei',
            'licença',
            'prefeitura',
        ]

        value = helper_test(self._categ, '20151215224404', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160114110247(self):
        expected = [
            'atendimento',
            'demora',
            'enfermeira',
            'gentileza',
            'medica',
            'posto',
        ]

        value = helper_test(self._categ, '20160114110247', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160114162712(self):
        expected = [
            'demora',
            'demorado',
            'emissão',
            'ippucspv',
            'pareceres',
            'planejamento viario',
        ]

        value = helper_test(self._categ, '20160114162712', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160318164800(self):
        expected = [
            'central 156',
            'coleta',
            'entulhos',
            'protocolo',
        ]

        value = helper_test(self._categ, '20160318164800', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160320024051(self):
        expected = [
            'protocolo',
            'pendente',
        ]

        value = helper_test(self._categ, '20160320024051', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160321084310(self):
        expected = [
            'fiscalização',
            'igreja',
            'licença',
            'protocolo central 156',
        ]

        value = helper_test(self._categ, '20160321084310', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160407145208(self):
        expected = [
            'agendamento seguro desemprego via',
            'agendamento',
            'agendar',
            'cidadania',
            'feira',
            'muita',
            'ruas',
            'seguro desemprego',
            'sine',
        ]

        value = helper_test(self._categ, '20160407145208', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160407151252(self):
        expected = [
            'agendamento seguro',
            'agendar seguro desemprego',
            'feira',
            'resposta',
        ]

        value = helper_test(self._categ, '20160407151252', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160407171141(self):
        expected = [
            'muita informação',
            'serviço',
            'iluminação',
            'central 156',
        ]

        value = helper_test(self._categ, '20160407171141', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160407171659(self):
        expected = [
            'atendimento',
            'central 156',
            'demora',
            'manutenção',
            'mato',
            'praça',
            'protocolo',
        ]

        value = helper_test(self._categ, '20160407171659', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160408104742(self):
        expected = [
            'academia',
            'aula',
            'aulas',
            'parque',
            'professores',
            'retiraram',
        ]

        value = helper_test(self._categ, '20160408104742', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160513171202(self):
        expected = [
            'atendimento',
            'falta',
            'ouvidoria',
            'protocolo pendente',
            'protocolo',
            'resposta',
        ]

        value = helper_test(self._categ, '20160513171202', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160513230846(self):
        expected = [
            'desvios',
            'doaçoes',
            'provopar',
        ]

        value = helper_test(self._categ, '20160513230846', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160519074250(self):
        expected = [
            'alvarás',
            'aprovação',
            'cobra propina',
            'fiscal cobra propina',
            'fiscal',
            'projetos',
            'smma',
        ]

        value = helper_test(self._categ, '20160519074250', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160520145243(self):
        expected = [
            'demora',
            'atendimento',
            'iluminação',
            'protocolo',
            'serviço',
            'falta',
        ]

        value = helper_test(self._categ, '20160520145243', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160621131403(self):
        expected = [
            'instalação',
            'relógio',
            'copel',
            'instalação copel',
        ]

        value = helper_test(self._categ, '20160621131403', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160621150059(self):
        expected = [
            'troca',
            'prefeitura',
            'lâmpada',
        ]

        value = helper_test(self._categ, '20160621150059', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160706195107(self):
        expected = [
            'agendar',
            'seguro desemprego',
        ]

        value = helper_test(self._categ, '20160706195107', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160706202213(self):
        expected = [
            'lampada',
            'queimada',
            'luminária',
            'rua',
            'protocolo',
        ]

        value = helper_test(self._categ, '20160706202213', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160707154823(self):
        expected = [
            'informação',
            'ouvidor',
        ]

        value = helper_test(self._categ, '20160707154823', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160707195609(self):
        expected = [
            'magistério',
            'pagamento',
            'prefeitura',
            'ldo',
            'funcionalismo'
        ]

        value = helper_test(self._categ, '20160707195609', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160708015922(self):
        expected = [
            'silencio',
            'trabalho',
            'prefeitura',
            'barulho',
            'lei',
            '156',
        ]

        value = helper_test(self._categ, '20160708015922', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160708091550(self):
        expected = [
            'cmei',
            'rua',
            'falta',
            'muita',
            'resposta',
            'serviço',
            'trabalho',
        ]

        value = helper_test(self._categ, '20160708091550', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160716000637(self):
        expected = [
            'atendimento rua',
            'atendimento',
            'carteira',
            'cidadania',
            'feira',
            'informação',
            'prefeitura',
            'serviço',
            'trabalho',
        ]

        value = helper_test(self._categ, '20160716000637', self._claims)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160716145306(self):
        expected = [
            'seguro',
            'seguro desemprego',

        ]

        value = helper_test(self._categ, '20160716145306', self._claims)
        self.assertEqual(sorted(expected), sorted(value))


if __name__ == '__main__':
    unittest.main()

