import dados
import rake

'''
import categoriza
claims = categoriza.categoriza_claims()
claims
claims['keywords']
set().union(claims['keywords'])
set().union(*claims['keywords'])
unicas = set().union(*claims['keywords'])
[u[0] for u in unicas]
unicas = set([u[0] for u in set().union(*claims['keywords'])])
unicas
with open('stoplists/all.txt', 'w') as tudo:
    for item in unicas:
        tudo.write('{}\n'.format(item))
'''


def categoriza_claims(categ, claims):
    for claim in claims:
        categoriza_claim(categ, claim)
    return claims


def categoriza_claim(categ, claim):
    if 'x20150701145318' in claim['uri']:
        import pdb; pdb.set_trace()
    if 'x20160216105543' in claim['uri']:
        import pdb; pdb.set_trace()
    if 'x20160219112156' in claim['uri']:
        import pdb; pdb.set_trace()

    texto = '{} - {}'.format(claim['title'], claim['description'])
    claim['keywords'] = categ.run(texto)
    return claim


def keywords_para_arquivo(arquivo, dados):
    with open(arquivo, 'w') as output:
        output.writelines(
            ('{0[uri]} - {0[keywords]}\n'.format(item) for item in dados))


def main(stoplist='stoplists/ouvidoria.txt'):
    categ = rake.Rake(stoplist)
    claims = dados.prepara_dados()
    claims = categoriza_claims(categ, claims)
    keywords_para_arquivo('/tmp/teste.txt', claims)
    for claim in claims:
        print(claim['uri'], claim['keywords'])


if __name__ == '__main__':
    main()
