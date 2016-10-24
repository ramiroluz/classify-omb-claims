#!/usr/bin/env python3

def claim_tags(keywords):
    kwset = set(keywords)
    if {'cortes', 'áreas verdes', 'árvores'}.issubset(kwset):
        return [
            'autorização de cortes de árvores',
            'publicação de dados',
            'sgm',
        ]
    elif {'poda', 'protocolo', 'árvore', 'árvores'}.issubset(kwset):
        return [
            'poda de árvores',
            'smma',
        ]
    elif (('seguro' in kwset or 'agendar' in kwset) and
          ('seguro desemprego' in kwset)):
        return [
            'agendamento de seguro desemprego',
            'smte',
        ]
    elif {'atendimento rua',
          'atendimento',
          'carteira',
          'cidadania',
          'feira',
          'informação',
          'prefeitura',
          'serviço',
          'trabalho',}.issubset(kwset):
        return [
            'mal atendimento',
            'rua da cidadania',
            'sgm',
        ]

    return ['iluminação pública', 'troca de lâmpadas', 'smop']
