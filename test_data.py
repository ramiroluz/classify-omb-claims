#!/usr/bin/env python

from collections import defaultdict

data = [
    ('20150618134915', 'sgm','falta de atendimento',),
    ('20150804104915', 'smop','erosão em galeria de águas pluviais'),
    ('20150618123604', 'comupa', 'falta de atendimento',),
    ('20150526123609', 'fas', 'atendimento a moradores de rua',),
    ('20150803112423', 'setran', 'fiscalização de trânsito',),
    ('20160329214149', 'omc', 'falta de atendimento',),
    ('20151215152445', 'setran', 'fiscalização de trânsito',),
    ('20150521091041', 'central 156',),
    ('20160401151335', 'smop', 'iluminação pública',),
    ('20150624113733', 'smma', 'limpeza de terreno',),
    ('20150624152440', 'sigiloso',),
    ('20150820090506', 'sgm', 'recuperação de tubulação',),
    ('20160310105617', 'smop', 'iluminação pública',),
    ('20160310110313', 'smma', 'coleta de lixo vegetal',),
    ('20160118170430', 'omc', 'falta de atendimento',),
    ('20150812163908', 'smop', 'iluminação pública',),
    ('20150910112005', 'smop', 'iluminação pública',),
    ('20151210152843', 'smop', 'iluminação pública',),
    ('20150819113029', 'smop', 'iluminação pública',),
    ('20160330112500', 'cohab', 'demora no atendimento'),
    ('20151001100204', 'smma', 'coleta de lixo vegetal',),
    ('20160125155421', 'smu', 'fiscalização de comércio',),
    ('20160408155145', 'smop', 'iluminação pública',),
    ('20150804104531', 'smma', 'coleta de lixo vegetal',),
    ('20160309115607', 'smop', 'iluminação pública',),
    ('20160601103836', 'urbs', 'transporte coletivo',),
    ('20151125100053', 'smma', 'remoção de toco',),
    ('20160125150017', 'smma', 'coleta de lixo vegetal',),
    ('20151029152659', 'smu', 'fiscalização de terreno',),
    ('20150702084208', 'smelj', 'área de lazer',),
    ('20160216115822', 'smop', 'caixa de captação',),
    ('20160329214149', 'omc', 'falta de atendimento',),
    ('20160409210448', 'sms', 'visita de equipe médica',),
    ('20160304160527', 'smma', 'limpeza terreno',),
    ('20160125150017', 'smma', 'coleta de lixo vegetal',),
    ('20151016082403', 'fiscalização',),
    ('20150521092645', 'smop', 'operação tapa buracos',),
    ('20150602154107', 'cmc', 'mal atendimento'),
    ('20150813173235', 'smma', 'poda de árvore'),
    ('20160311140658', 'smma', 'coleta de caliça',),
    ('20150914142238', 'smma', 'coleta de lixo vegetal',),
    ('20150521085108', 'cmc', 'projeto de lei',),
    ('20150818150225', 'smop', 'operação tapa buracos',),
    ('20150713103429', 'smop', 'iluminação pública',),
    ('20151120105605', 'sgm', 'abertura de rua',),
    ('20160318153937', 'smop', 'iluminação pública',),
    ('20150803112423', 'setran', 'fiscalização de trânsito',),
    ('20150526123726', 'central 156', 'falta de atendimento',),
    ('20160318152111', 'smma', 'coleta de lixo vegetal',),
    ('20160113145621', 'smma', 'coleta de caliça',),
    ('20160128121251', 'smf', 'iptu',),
    ('20150911133111', 'smop', 'iluminação pública',),
    ('20150721163536', 'smop', 'iluminação pública',),
    ('20150728145753', 'smop', 'iluminação pública',),
    ('20151226191455', 'omc', 'prazo para resposta',),
    ('20151001100255', 'smop', 'iluminação pública',),
    ('20160218162110', 'smop', 'caixa de captação',),
    ('20151006103225', 'smu', 'fiscalização de terreno',),
    ('20150805151335', 'smma', 'poda de árvore',),
    ('20150819104316', 'smop', 'iluminação pública',),
    ('20160530155012', 'omc', 'transparência',),
    ('20160603110306', 'smop', 'iluminação pública',),
    ('20150817155325', 'setran', 'acessibilidade',),
    ('20150720085945', 'smma', 'coleta de lixo vegetal',),
    ('20150917104714', 'smma', 'coleta de lixo vegetal',),
    ('20151111083243', 'omc', 'falta de atendimento',),
    ('20160602150135', 'smop', 'iluminação pública',),
    ('20150720110750', 'smop', 'iluminação pública',),
    ('20151204145848', 'smop', 'iluminação pública',),
    ('20150522105759', 'omc', 'regulamentação de lei',),
    ('20151016112813', 'urbs', 'bom atendimento',),
    ('20150520134542', 'sgm', 'transparência',),
    ('20150521081032', 'omc',),
    ('20150521085957', 'central 156', 'falta de atendimento',),
    ('20150521090454', 'central 156', 'bom atendimento',),
    ('20150521091041', 'central 156', 'falta de atendimento',),
    ('20150521091537', 'sms', 'mal atendimento',),
    ('20150521091952', 'falta de aulas',),
    ('20150618095403', 'pmc', 'legislação municipal',),
    ('20150624152440', 'sigiloso',),
    ('20150624152928', 'omc', 'pedido de orientação',),
    ('20150720132602', 'imt', 'feira de artesanato',),
    ('20150721094934', 'smelj', 'atividade de lazer'),
    ('20150805151819', 'smma', 'fiscalização de saneamento',),
    ('20150805153014', 'smelj', 'atividade de lazer',),
    ('20150805190247', 'omc', 'falta de atendimento',),
    ('20150824151751', 'smop', 'implantação de antipó',),
    ('20150825143854', 'sms', 'criação de animais',),
    ('20150827172206', 'urbs', 'trasnporte coletivo',),
    ('20150830031023', 'smelj', 'área de lazer',),
    ('20151007145751', 'omc', 'falta de atendimento',),
    ('20151007145802', 'omc', 'falta de atendimento',),
    ('20151007145805', 'omc', 'falta de atendimento',),
    ('20151007195233', 'omc', 'falta de atendimento',),
    ('20151211160022', 'smop', 'caixa de captação',),
    ('20151212123927', 'setran', 'bloqueio de rua',),
    ('20151215223622', 'sme', 'vagas em cemei',),
    ('20151215224404', 'sme', 'vagas em cemei',),
    ('20160114110247', 'sms','bom atendimento',),
    ('20160114162712', 'ippuc', 'demora no atendimento',),
    ('20160320024051', 'omc', 'falta de atendimento',),
    ('20160407151252', 'smte', 'seguro desemprego',),
    ('20160407171141', 'smop', 'iluminação pública',),
    ('20160513230846', 'provopar', 'desvio de doações',),
    ('20160621131403', 'copel', 'instalação de relógio',),
    ('20160706195107', 'smte', 'seguro desemprego',),
    ('20160706202213', 'smop', 'iluminação pública',),
    ('20160707154823', 'omc',),
    ('20160707195609', 'sme', 'transparência',),
    ('20160708015922', 'urbs', 'poluição sonora'),
    ('20160708091550', 'sme','vagas em cmei',),
    ('20160716000637', 'sgm','mal atendimento',),
    ('20160716145306', 'smte','seguro desemprego',),
]

categories = defaultdict(list)
url_template = 'http://www.ouvidoria.curitiba.pr.leg.br/ouvidoria/{}'
for item in data:
    categories[','.join(item[1:])].append(url_template.format(item[0])) 
