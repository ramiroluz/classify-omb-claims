#!/usr/bin/env python3

import bayes
import categoriza

bT = bayes.BayesText()
bT.compute()
claims = categoriza.dados.prepara_dados()
claim_urls = [
    'http://www.ouvidoria.curitiba.pr.leg.br/ouvidoria/20160607101205',
    'http://www.ouvidoria.curitiba.pr.leg.br/ouvidoria/20160601154604'
]

claims = [claim for claim in claims if claim['uri'] in claim_urls]

stopwordlist='stoplists/ouvidoria.txt'
categ = categoriza.rake.Rake(stopwordlist)

claims = categoriza.categoriza_claims(categ, claims)

bT.classify(claims[0])
bT.classify(claims[1])
