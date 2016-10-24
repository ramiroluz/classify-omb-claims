#!/usr/bin/env python3

import unittest
import bayes


class TestBayes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bayes_text = bayes.BayesText()
        cls.bayes_text.compute()

    def test_claims(self):
        self.assertEqual(len(self.bayes_text.claims), 446)

    def test_trained_data(self):
        self.assertEqual(len(self.bayes_text.trained_data), 446)

    def test_categories(self):
        self.assertEqual(len(self.bayes_text.categories), 120)


if __name__ == '__main__':
    unittest.main()

