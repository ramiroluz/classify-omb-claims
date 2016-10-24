#!/usr/bin/env python3

import unittest
from tags import claim_tags


class TestCategoriza(unittest.TestCase):
    def test_20150618134915(self):
        keywords = [
            '156',
            'administração municipal',
            'central 156',
            'gestão municipal',
            'gestão',
            'ouvidoria',
            'protocolo',
            'resposta',
            'serviço público',
            'transparência',
            'área',
        ]

        expected = [
            'encerramento sem serviço',
            'central 156',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150804104915(self):
        keywords = [
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

        expected = [
            'erosão em galeria de águas pluviais',
            'sgm',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150618123604(self):
        keywords = [
            '156',
            'central 156',
            'comupa',
            'ouvidoria',
            'resposta',
            'sgm',
        ]

        expected = [
            'sgm',
            'comupa',
            'encerramento sem serviço',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150526123609(self):
        keywords = [
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

        expected = [
            'atendimento de moradores de rua',
            'animais abandonados',
            'central 156',
            'fas',
            'smds',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150803112423(self):
        keywords = [
            'central 156',
            '156',
            'falta',
            'fiscalização',
            'trânsito',
            'setran',
            'agentes',
        ]

        expected = [
            'fiscalização de trânsito',
            'setran',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160329214149(self):
        keywords = [
            'ouvidoria',
            '156',
            'prefeitura',
        ]

        expected = [
            'central 156',
            'ouvidoria',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151215152445(self):
        keywords = [
            'atendimento setran',
            'central 156',
            'falta',
            'fiscalização',
            'fiscalizações',
            'ouvidor',
            'setran',
            'transito',
        ]

        expected = [
            'fiscalização de trânsito',
            'setran',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150521091041(self):
        keywords = [
            'central 156',
        ]

        expected = [
            'central 156',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160401151335(self):
        keywords = [
            'central 156',
            'demora',
            'iluminação pública',
            'lâmpada',
            'protocolo',
            'saúde',
            'troca',
            'unidade',
        ]

        expected = [
            'iluminação pública',
            'troca de lâmpada',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150624113733(self):
        keywords = [
            'roçada',
            'mato',
            '156', 
        ]

        expected = [
            'roçada de terreno',
            'sgm',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150624152440(self):
        keywords = [
            'sigiloso',
        ]

        expected = [
            'sigiloso',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150820090506(self):
        keywords = [
            'calçada',
            'criação',
            'drenagem',
            'obra',
            'prefeitura',
            'protocolo',
            'recuperação',
            'tubulação',
            'pública',
            'resposta',
            'unidade',
        ]

        expected = [
            'recuperação de tubulação',
            'sgm',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160310105617(self):
        keywords = [
            'iluminação pública',
            'lâmpada queimada',
            'protocolo central 156',
            'troca',
        ]

        expected = [
            'iluminação pública',
            'troca de lâmpada',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160310110313(self):
        keywords = [
            'coleta',
            'lixo vegetal',
            'protocolo central 156',
        ]

        expected = [
            'coleta de lixo vegetal',
            'smma',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160118170430(self):
        keywords = [
            'atendida',
            'ouvidoria',
            'protocolo',
            'urbs',
        ]

        expected = [
            'ouvidoria',
            'urbs',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150812163908(self):
        keywords = [
            'central 156',
            'lâmpadas',
            'manutenção',
            'protocolo',
            'troca',
        ]

        expected = [
            'iluminação pública',
            'troca de lâmpada',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150910112005(self):
        keywords = [
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

        expected = [
            'iluminação pública',
            'troca de lâmpada',
            'manutenção de luminária',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151210152843(self):
        keywords = [
            'central 156',
            'demora',
            'iluminação pública',
            'lâmpada',
            'protocolo',
        ]

        expected = [
            'iluminação pública',
            'troca de lâmpada',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150819113029(self):
        keywords = [
            'central 156',
            'iluminação pública',
            'lâmpadas',
            'rua',
            'troca',
        ]

        expected = [
            'iluminação pública',
            'troca de lâmpada',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160330112500(self):
        keywords = [
            'atendimento',
            'central 156',
            'cohab',
            'demora',
            'menores',
            'moradia popular',
            'prefeitura',
            'protocolo',
        ]

        expected = [
            'moradia popular',
            'cohab',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151001100204(self):
        keywords = [
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

        expected = [
            'coleta de lixo',
            'smma',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160125155421(self):
        keywords = [
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

        expected = [
            'fiscalização de comércio',
            'smu',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160408155145(self):
        keywords = [
            'atendimento',
            'central 156',
            'demora',
            'iluminação pública',
            'protocolo',
        ]

        expected = [
            'iluminação pública',
            'troca de lâmpada',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150804104531(self):
        keywords = [
            'atendimento',
            'coleta',
            'criação',
            'jardim',
            'lixo vegetal',
            'protocolo',
            'resíduos vegetais',
        ]

        expected = [
            'coleta de lixo vegetal',
            'smma',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160309115607(self):
        keywords = [
            'iluminação pública',
            'lâmpadas queimadas',
            'protocolo central 156',
            'publicidade',
            'troca',
        ]

        expected = [
            'iluminação pública',
            'troca de lâmpada',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160601103836(self):
        keywords = [
            'atraso',
            'atrasos',
            'gentileza',
            'linha',
            'motorista',
        ]

        expected = [
            'atraso de ônibus',
            'transporte coletivo',
            'urbs',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151125100053(self):
        keywords = [
            'corte',
            'árvore',
            'central 156',
            'prefeitura',
            'toco',
        ]

        expected = [
            'remoção de toco',
            'smma',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160125150017(self):
        keywords = [
            'coleta',
            'lixo vegetal',
            'central 156',
        ]

        expected = [
            'coleta de lixo vegetal',
            'smma',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151029152659(self):
        keywords = [
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

        expected = [
            'fiscalização de terreno',
            'smu',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150702084208(self):
        keywords = [
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

        expected = [
            'implantação de área de lazer',
            'smelj',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160216115822(self):
        keywords = [
            '156',
            'caixa',
            'captação',
            'falta',
            'orientação',
            'público',
            'relocação',
            'resposta',
        ]

        expected = [
            'caixa de captação',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160329214149(self):
        keywords = [
            '156',
            'ouvidoria',
            'prefeitura',
            'público',
            'serviço 156',
        ]

        expected = [
            'central 156',
            'ouvidoria',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160409210448(self):
        keywords = [
            'agendamento',
            'alcoólica',
            'hospital',
            'saúde',
            'unidade básica',
        ]

        expected = [
            'visita de equipe multidisciplinar',
            'hospital zilda arns',
            'sms',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160304160527(self):
        keywords = [
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

        expected = [
            'limpeza terreno',
            'mosquito da dengue',
            'smu',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160125150017(self):
        keywords = [
            'atendida',
            'central 156',
            'coleta',
            'demora',
            'lixo vegetal',
            'protocolo',
            'serviço',
        ]

        expected = [
            'coleta de lixo vegetal',
            'smma',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151016082403(self):
        keywords = [
            '156',
            'fiscalização',
            'protocolo 156',
            'protocolo',
        ]

        expected = [
            'fiscalização',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150521092645(self):
        keywords = [
            'asfalto',
            'buracos',
            'manutenção',
            'rua',
            'transito',
            'veículos',
        ]

        expected = [
            'operação tapa buracos',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150602154107(self):
        keywords = [
            'atendeu mal',
            'mal atendimento',
            'pública',
        ]

        expected = [
            'mal atendimento',
            'cmc',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150813173235(self):
        keywords = [
            'central 156',
            'galhos',
            'poda',
            'público',
            'resposta',
            'rua',
            'árvore',
        ]

        expected = [
            'poda de árvore',
            'smma',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160311140658(self):
        keywords = [
            'caliça',
            'central 156',
            'coleta',
            'demora',
            'dengue',
            'mosquito',
            'protocolo',
            'recolhimento',
        ]

        expected = [
            'coleta de caliça',
            'mosquito da dengue',
            'smma',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150914142238(self):
        keywords = [
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

        expected = [
            'coleta de lixo vegetal',
            'smma',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150521085108(self):
        keywords = [
            'bebida alcoólica',
            'bebidas',
            'estádios',
            'lei',
            'futebol',
            'vereadores',
        ]

        expected = [
            'projeto de lei',
            'vereadores',
            'cmc',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150818150225(self):
        keywords = [
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

        expected = [
            'operação tapa buracos',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150713103429(self):
        keywords = [
            'atendimento',
            'central 156',
            'iluminação pública',
            'protocolo',
            'rua',
        ]

        expected = [
            'iluminação pública',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151120105605(self):
        keywords = [
            'central 156',
            'fechamento',
            'via',
            'moradores',
            'preservação',
            'protocolo',
            'rua',
            'área',
        ]

        expected = [
            'fechamento de via',
            'sgm',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160318153937(self):
        keywords = [
            'atendimento',
            'central 156',
            'iluminação pública',
            'iluminação',
            'protocolo',
        ]

        expected = [
            'iluminação pública',
            'manutenção de luminária',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150803112423(self):
        keywords = [
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

        expected = [
            'fiscalização de trânsito',
            'setran',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150526123726(self):
        keywords = [
            '156',
            'falta',
            'ouvidoria',
            'respsotas',
            'via central 156',
        ]

        expected = [
            'central 156',
            'falta de resposta',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160318152111(self):
        keywords = [
            'atendimento',
            'central 156',
            'coleta',
            'demora',
            'galhos',
            'protocolo',
        ]

        expected = [
            'coleta de lixo vegetal',
            'smma',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160113145621(self):
        keywords = [
            'caliça',
            'central 156',
            'demora',
            'protocolo',
            'recolhimento',
            'rua',
            'serviço',
        ]

        expected = [
            'coleta de caliça',
            'smma',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160128121251(self):
        keywords = [
            '156',
            'informação',
            'iptu',
            'meio ambiente',
            'prefeitura',
            'preservação',
            'protocolo',
            'resposta',
            'área',
        ]

        expected = [
            'redução do iptu',
            'smma',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150911133111(self):
        keywords = [
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

        expected = [
            'iluminação pública',
            'troca de lâmpada',
            'manutenção de luminárias',
            'smma',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150721163536(self):
        keywords = [
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

        expected = [
            'iluminação pública',
            'troca de lâmpada',
            'manutenção de luminárias',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150728145753(self):
        keywords = [
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

        expected = [
            'iluminação pública',
            'troca de lâmpada',
            'manutenção de luminárias',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151226191455(self):
        keywords = [
            '156',
            'demora',
            'denúncia',
            'ouvidoria',
            'protocolo',
            'resposta',
        ]

        expected = [
            'prazo para resposta',
            'ouvidoria',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151001100255(self):
        keywords = [
            'atendimento',
            'iluminação pública',
            'luminária',
            'lâmpada',
            'manutenção',
            'protocolo',
            'queimada',
            'rua',
        ]

        expected = [
            'iluminação pública',
            'troca de lâmpada',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160218162110(self):
        keywords = [
            'caixa',
            'captação',
            'limpeza',
            'protocolo 156',
            'resposta',
        ]

        expected = [
            'caixa de captação',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151006103225(self):
        keywords = [
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

        expected = [
            'invasão de área pública',
            'fiscalização de terreno',
            'smu',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150805151335(self):
        keywords = [
            'poda',
            'protocolo',
            'árvore',
            'árvores',
        ]

        expected = [
            'poda de árvore',
            'smma',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150819104316(self):
        keywords = [
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

        expected = [
            'iluminação pública',
            'troca de lâmpada',
            'manutenção de luminárias',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160530155012(self):
        keywords = [
            'atividades',
            'lei',
            'lei lei',
            'ouvidor',
            'relatório',
            'relatório circunstanciado',
            'ouvidoria municipal',
        ]

        expected = [
            'publicação de dados',
            'ouvidoria',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160603110306(self):
        keywords = [
            'iluminação pública',
            'central 156',
            'protocolo',
            'serviço',
        ]

        expected = [
            'ressarcimento de taxa',
            'iluminação pública',
            'sgm',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150817155325(self):
        keywords = [
            'criação',
            'deficientes',
            'implantação',
            'protocolo',
            'rio',
            'unidade',
            'vagas',
        ]

        expected = [
            'implantação de vagas para deficiênte',
            'setran',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150720085945(self):
        keywords = [
            'atendimento',
            'coleta',
            'jardim',
            'lixo vegetal',
            'meio',
            'protocolo',
            'resíduos vegetais',
            'unidade',
        ]

        expected = [
            'coleta de lixo vegetal',
            'smma',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150917104714(self):
        keywords = [
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

        expected = [
            'coleta de lixo vegetal',
            'smma',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151111083243(self):
        keywords = [
            '156',
            'mal',
            'municipais',
            'ouvidoria municipal',
            'ouvidoria',
            'protocolo 156',
            'protocolo',
            'resposta',
        ]

        expected = [
            'ouvidoria',
            'central 156',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160602150135(self):
        keywords = [
            'falta',
            'iluminação pública',
            'iluminação',
        ]

        expected = [
            'iluminação pública',
            'isenção de taxa',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150720110750(self):
        keywords = [
            'iluminação',
            'implantação',
            'luminária',
            'meio',
            'moradores',
            'praça',
            'protocolo',
            'unidade',
        ]

        expected = [
            'iluminação pública',
            'implantação de luminária',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151204145848(self):
        keywords = [
            'atendimento',
            'iluminação pública',
            'lâmpada',
            'protocolo 156',
            'rua',
            'serviço',
            'troca',
        ]

        expected = [
            'iluminação pública',
            'troca de lâmpada',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150522105759(self):
        keywords = [
            'lei',
            'lei municipal',
            'logradouros públicos',
            'abandono',
            'veículos',
        ]

        expected = [
            'lei municipal',
            'abandono de veículos',
            'ouvidoria',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151016112813(self):
        keywords = [
            'exemplar',
            'meio',
            'motorista',
            'praça',
            'ônibus',
        ]

        expected = [
            'bom atendimento',
            'motorista exemplar',
            'urbs',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150520134542(self):
        keywords = [
            'cortes',
            'áreas verdes',
            'árvores',
        ]

        expected = [
            'autorização de cortes de árvores',
            'publicação de dados',
            'sgm',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150521081032(self):
        keywords = [
            'ouvidoria',
            '156',
        ]

        expected = [
            'ouvidoria',
            'central 156',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150521085957(self):
        keywords = [
            '156',
        ]

        expected = [
            'central 156',
            'sgm',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150521090454(self):
        keywords = [
            '156',
            'atendida',
            'serviço',
        ]

        expected = [
            'sgm',
            'central 156',
            'bom atendimento',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150521091041(self):
        keywords = [
            '156',
        ]

        expected = [
            'central 156',
            'sgm',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150521091537(self):
        keywords = [
            'funcionario',
            'posto',
            'saude',
        ]

        expected = [
            'mal atendimento',
            'ubs',
            'sms',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150521091952(self):
        keywords = [
            'aula',
            'aulas',
            'ouvidoria',
        ]

        expected = [
            'falta de aulas',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150618095403(self):
        keywords = [
            'calçadas',
            'lei',
            'lixeiras irregulares',
            'lixeiras',
        ]

        expected = [
            'lixeiras irregulares',
            'smu',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150624152440(self):
        keywords = [
            'sigiloso',
            'orientação',
        ]

        expected = [
            'sigiloso',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150624152928(self):
        keywords = [
            'orientação',
        ]

        expected = [
            'pedido de orientação',
            'ouvidoria',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150720132602(self):
        keywords = [
            'feira',
            'largo',
            'ordem',
        ]

        expected = [
            'pedido de informação',
            'imt',
            'feira de artesanato',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150721094934(self):
        keywords = [
            'atividades',
            'falta',
            'idoso',
            'medicamentos',
            'medicações',
            'postos',
            'saúde',
        ]

        expected = [
            'falta de medicamento',
            'atividades para idoso',
            'sms',
            'smelj',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150805151819(self):
        keywords = [
            'esgoto',
            'smma',
        ]

        expected = [
            'vazamento de esgoto',
            'smma',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150805153014(self):
        keywords = [
            'atividades',
            'aulas',
            'cidadania',
            'ginástica',
            'rua',
            'smelj',
            'suspensão',
            'terceira idade',
        ]

        expected = [
            'atividades para idoso',
            'smelj',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150805190247(self):
        keywords = [
            'ouvidor',
            'ouvidoria',
            'protocolo',
            'resposta',
        ]

        expected = [
            'ouvidoria',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150824151751(self):
        keywords = [
            'revestimento asfáltico',
            'rua',
            'ruas',
        ]

        expected = [
            'revestimento asfáltico',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150825143854(self):
        keywords = [
            'criação',
            'animais',
            'zona residencial',
        ]

        expected = [
            'criação de animais',
            'sms',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150827172206(self):
        keywords = [
            'cartão transporte',
            'cartão',
            'idade',
            'renovação',
            'transporte',
            'urbs',
        ]

        expected = [
            'cartão transporte',
            'transporte coletivo',
            'urbs',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20150830031023(self):
        keywords = [
            'academia',
            'central 156',
            'implantação',
            'licença',
            'praça',
            'protocolo',
            'resposta'
        ]

        expected = [
            'ginástica ao ar livre',
            'implantar área de lazer',
            'smelj',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151007145751(self):
        keywords = [
            'resposta',
            'denúncia',
        ]

        expected = [
            'resposta de solicitação',
            'ouvidoria',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151007145802(self):
        keywords = [
            'resposta',
            'denúncia',
        ]

        expected = [
            'resposta de solicitação',
            'ouvidoria',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151007145805(self):
        keywords = [
            'resposta',
            'denúncia',
        ]

        expected = [
            'resposta de solicitação',
            'ouvidoria',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151007195233(self):
        keywords = [
            'atendimento',
            'caixa',
            'iluminação pública',
            'resposta',
        ]

        expected = [
            'resposta de solicitação',
            'iluminação pública',
            'ouvidoria',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151211160022(self):
        keywords = [
            'desobstrução',
            'bueiro',
        ]

        expected = [
            'desobstrução de bueiro',
            'sgm',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151212123927(self):
        keywords = [
            'bloqueios',
            'fechamentos',
            'pedreira',
            'pública',
            'ruas',
            'terceira',
        ]

        expected = [
            'bloqueio de rua',
            'setran',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151215223622(self):
        keywords = [
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

        expected = [
            'fechamento de berçário',
            'cemei',
            'sme',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20151215224404(self):
        keywords = [
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

        expected = [
            'fechamento de berçário',
            'cemei',
            'sme',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160114110247(self):
        keywords = [
            'atendimento',
            'demora',
            'enfermeira',
            'gentileza',
            'medica',
            'posto',
        ]

        expected = [
            'bom atendimento',
            'ubs',
            'sms',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160114162712(self):
        keywords = [
            'demora',
            'demorado',
            'emissão',
            'ippucspv',
            'pareceres',
            'planejamento viario',
        ]

        expected = [
            'demora na emissão de parecer',
            'ippuc',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160320024051(self):
        keywords = [
            'protocolo',
            'pendente',
        ]

        expected = [
            'protocolo pendente',
            'ouvidoria',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160407151252(self):
        keywords = [
            'agendamento seguro',
            'agendar seguro desemprego',
            'feira',
            'resposta',
        ]

        expected = [
            'agendamento de seguro desemprego',
            'smte',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160407171141(self):
        keywords = [
            'muita informação',
            'serviço',
            'iluminação',
            'central 156',
        ]

        expected = [
            'central 156',
            'iluminação pública',
            'solicita muita informação',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160513230846(self):
        keywords = [
            'desvios',
            'doaçoes',
            'provopar',
        ]

        expected = [
            'desvio de doações',
            'provopar',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160621131403(self):
        keywords = [
            'instalação',
            'relógio',
            'copel',
            'instalação copel',
        ]

        expected = [
            'serviço estadual',
            'copel',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160706195107(self):
        keywords = [
            'agendar',
            'seguro desemprego',
        ]

        expected = [
            'agendamento de seguro desemprego',
            'smte',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160706202213(self):
        keywords = [
            'lampada',
            'queimada',
            'luminária',
            'rua',
            'protocolo',
        ]

        expected = [
            'iluminação pública',
            'manutenção de luminária',
            'troca de lâmpada',
            'smop',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160707154823(self):
        keywords = [
            'informação',
            'ouvidor',
        ]

        expected = [
            'pedido de informação',
            'ouvidoria',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160707195609(self):
        keywords = [
            'magistério',
            'pagamento',
            'prefeitura',
            'ldo',
            'funcionalismo'
        ]

        expected = [
            'ldo',
            'publicação de dados',
            'sme',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160708015922(self):
        keywords = [
            'silencio',
            'trabalho',
            'prefeitura',
            'barulho',
            'lei',
            '156',
        ]

        expected = [
            'lei do silêncio',
            'limpeza de terminal',
            'urbs',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160708091550(self):
        keywords = [
            'cmei',
            'rua',
            'falta',
            'muita',
            'resposta',
            'serviço',
            'trabalho',
        ]

        expected = [
            'vaga em cmei',
            'sme',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160716000637(self):
        keywords = [
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

        expected = [
            'mal atendimento',
            'rua da cidadania',
            'sgm',
        ]

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))

    def test_20160716145306(self):
        keywords = [
            'seguro',
            'seguro desemprego',
        ]

        expected = [
            'agendamento de seguro desemprego',
            'smte',
        ] 

        value = claim_tags(keywords)
        self.assertEqual(sorted(expected), sorted(value))


if __name__ == '__main__':
    unittest.main()

