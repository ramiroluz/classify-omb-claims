import os
import codecs
import math
import categoriza
from collections import defaultdict
from collections import Counter


DEBUG = True
DEBUG = False

class BayesText:
    def __init__(self, stopwordlist='stoplists/ouvidoria.txt'):
        """This class implements a naive Bayes approach to text
        classification
        """

        self.DEBUG = DEBUG

        self.stoplist = stopwordlist
        self.categ = categoriza.rake.Rake(self.stoplist)

        self.claims = []
        self.trained_data = []
        self.categories = []
        self.vocabulary = Counter()
        self.prob = Counter()
        self.totals = Counter()

    def compute(self):
        self.init_train_data()
        self.init_claims()
        self.init_categories()
        self.init_keywords()

        self.count_keywords()

        self.compute_probabilities()
        print ("DONE TRAINING\n\n")

    def init_train_data(self):
        with open('train_source.txt') as train_source:
            trained_source = train_source.readlines()
        
        trained_data = [x.split('-') for x in trained_source]
        trained_data = [(x[0].strip(), x[1].strip().split('|'),) for x in trained_data]

        self.trained_data = trained_data

        return trained_data

    def init_claims(self):
        claims = categoriza.dados.prepara_dados()
        urls = [x[0] for x in self.trained_data]
        if urls:
            claims = [
                claim for claim in claims if claim['uri'] in urls
            ]
        claim_urls = [claim['uri'] for claim in claims] 
        missing = [url for url in urls if url not in claim_urls]
        self.claims = claims

        return claims

    def init_categories(self):
        """This first attempt will consider a category a set of tags."""

        categories = defaultdict(list)
        for item in self.trained_data:
            cat = ','.join(item[1])
            categories[cat].append(item[0])

        self.categories = categories
        return categories

    def init_keywords(self):
        '''After the categorization, each claim will have a
        keywords attribute.''' 

        claims = categoriza.categoriza_claims(self.categ, self.claims)
        self.claims = claims
        return claims

    def count_keywords(self):
        print("Counting ...")
        for category in self.categories:
            print('    {}'.format(category))
            (self.prob[category],
             self.totals[category]) = self.train(category)
        # I am going to eliminate any word in the vocabulary
        # that doesn't occur at least 3 times
        # toDelete = []
        # for word in self.vocabulary:
        #     if self.vocabulary[word] < 3:
                # mark word for deletion
                # can't delete now because you can't delete
                # from a list you are currently iterating over
                # toDelete.append(word)
        #        print('toDelete.append({})'.format(word))
        # now delete
        # for word in toDelete:
        #    del self.vocabulary[word]

    def train(self, category):
        """counts word occurrences for a particular category"""
        def trained_claim_categ(claim):
            trained = [x for x in self.trained_data if x[0] == claim['uri']]
            first = trained[0]
            tags = first[1]
            return ','.join(tags)

        counts = Counter()
        total = 0

        claims_of_category = [
            c for c in self.claims if trained_claim_categ(c) == category
        ]

        for claim in claims_of_category:
            # Each keywords item is a tuple. The first element is
            # the word and the second is its rank.
            tokens = []
            for keyword in [x[0] for x in claim['keywords']]:
                for item in keyword.split():
                    tokens.append(item)
            for token in tokens:
                self.vocabulary[token] += 1
                counts[token] += 1
                total += 1
        return (counts, total,)

    def compute_probabilities(self):
        # now compute probabilities
        vocabLength = len(self.vocabulary)
        print("Computing probabilities:")
        for category in self.categories:
            print('    {}'.format(category))
            denominator = self.totals[category] + vocabLength
            for word in self.vocabulary:
                if word in self.prob[category]:
                    count = self.prob[category][word]
                else:
                    count = 1
                self.prob[category][word] = (float(count + 1)
                                             / denominator)

    def classify(self, claim):
        results = defaultdict(int)
        # I think I don't need this loop because I am using DefaultDict.
        # for category in self.categories:
        #     results[category] = 0
        # Each keywords item is a tuple. The first element is
        # the word and the second is its rank.
        tokens = []
        for keyword in [x[0] for x in claim['keywords']]:
            for item in keyword.split():
                tokens.append(item)

        not_found = []
        for token in tokens:
            if token in self.vocabulary:
                for category in self.categories:
                    if self.prob[category][token] == 0:
                        print("%s %s" % (category, token))

                    results[category] += math.log(
                        self.prob[category][token])
            else:
                not_found.append(token)

        results = list(results.items())

        if not_found:
            print('Tokens not in vocubulary: {}'.format(
                ', '.join(not_found)
            ))

        if len(results) < 1:
            return 'Token not found'

        results.sort(key=lambda tuple: tuple[1], reverse=True)
        # for debugging I can change this to give me the entire list
        categ = 'Token not found, {}'.format(results[0][0]) if not_found else results[0][0]

        return categ

    def testCategory(self, claim_urls, category):
        claims = categoriza.dados.prepara_dados()
        claims = [claim for claim in claims if claim['uri'] in claim_urls]
        claims = categoriza.categoriza_claims(self.categ, claims)

        total = 0
        correct = 0
        for claim in claims:
            total += 1
            result = self.classify(claim)
            if result == category:
                correct += 1
            else:
                print()
                print(claim['uri'])
                print(claim['keywords'])
                print('Resultado: ', result)
                print('Esperado: ', category)
                print()

        return (correct, total)

    def test(self):
        """This first attempt will consider a category a set of tags.
        The tests were created before the idea of this algorithm, so
        the tags are a list. To the effect of this test the tags will
        be joined by comma.
        """
        correct = 0
        total = 0

        for category, claim_urls in self.categories.items():
            (catCorrect, catTotal) = self.testCategory(claim_urls, category)
            correct += catCorrect
            total += catTotal

        percent = (float(correct) / total) * 100
        message = "\n\nAccuracy is {:f}%  ({:d} test instances)"

        print(message.format(percent, total))

    def test_from_data(self):
        import test_data
        correct = 0
        total = 0

        for category, claim_urls in test_data.categories.items():
            (catCorrect, catTotal) = self.testCategory(claim_urls, category)
            correct += catCorrect
            total += catTotal

        percent = (float(correct) / total) * 100
        message = "\n\nAccuracy is {:f}%  ({:d} test instances)"

        print(message.format(percent, total))



if __name__ == '__main__':
    bT = BayesText()
    bT.compute()
    print("Running Test ...")
    bT.test()
    # bT.test_from_data()
