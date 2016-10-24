#!/usr/bin/env python3

from dados import prepara_dados
import bayes
import rake
import categoriza
from pprint import pprint


def get_claims_to_categorize(trained_data):
    categ = rake.Rake('stoplists/ouvidoria.txt')
    claims = prepara_dados()
    urls = [x[0] for x in trained_data]
    if urls:
        claims = [
            claim for claim in claims if claim['uri'] not in urls
        ]

    claims = categoriza.categoriza_claims(categ, claims)

    return claims


if __name__ == '__main__':
    bt = bayes.BayesText()
    bt.compute()
    claims = get_claims_to_categorize(bt.trained_data)
    for claim in claims:

        result = bt.classify(claim)
        print('{} - {}'.format(claim['uri'], result))
        if result.startswith('Token not found'):
            pprint('-'*50)
            pprint(claim['title'])
            pprint(claim['description'])
            pprint(claim['keywords'])
            pprint(sorted(set(claim['description'].split())))
