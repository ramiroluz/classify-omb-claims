# Implementation of RAKE - Rapid Automtic Keyword Exraction algorithm
# as described in:
# Rose, S., D. Engel, N. Cramer, and W. Cowley (2010). 
# Automatic keyword extraction from indi-vidual documents. 
# In M. W. Berry and J. Kogan (Eds.), Text Mining: Applications and Theory.unknown: John Wiley and Sons, Ltd.

import re
import operator

debug = False
test = True


def is_number(s):
    try:
        float(s) if '.' in s else int(s)
        return True
    except ValueError:
        return False


def load_stop_words(stop_word_file):
    """
    Utility function to load stop words from a file and return as a list of words
    @param stop_word_file Path and file name of a file containing stop words.
    @return list A list of stop words.
    """
    stop_words = []
    with open(stop_word_file) as swfile:
        for line in swfile:
            if line.strip()[0:1] != "#":
                for word in line.split():  # in case more than one per line
                    stop_words.append(word)
    return stop_words


def separate_words(text, min_word_return_size):
    """
    Utility function to return a list of all words that are have a length greater than a specified number of characters.
    @param text The text that must be split in to words.
    @param min_word_return_size The minimum no of characters a word must have to be included.
    """
    splitter = re.compile('[^\w_\\+\\-]', re.UNICODE)
    words = []
    for single_word in splitter.split(text):
        current_word = single_word.strip().lower()
        #leave numbers in phrase, but don't count as words, since they tend to invalidate scores of their phrases
        if len(current_word) > min_word_return_size and current_word != '' and not is_number(current_word):
            words.append(current_word)
    return words


def split_sentences(text):
    """
    Utility function to return a list of sentences.
    @param text The text that must be split in to sentences.
    """
    sentence_delimiters = re.compile('[.!?,;:\t\\\\"\\(\\)\\\'\u2019\u2013]|\\s\\-\\s')
    sentences = sentence_delimiters.split(text)
    return sentences


def remove_garbage(text):
    garbage = u'[\u2060\u202a\u200e\u202c]+'
    return re.sub(garbage, '', text)


def remove_urls_and_emails(text):
    # Remove urls and emails.
    # http://stackoverflow.com/questions/827557/how-do-you-validate-a-url-with-a-regular-expression-in-python
    url_regex = (
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)*$'
    )
    # http://stackoverflow.com/questions/6883049/regex-to-find-urls-in-string-in-python
    url_regex = (
        'http[s]?://(?:[a-zA-Z]|[0-9]|'
        '[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    )

    email_regex = r'[\w.-]+@[\w.-]+.\w+'

    text = re.sub(url_regex, '', text)
    text = re.sub(email_regex, '', text)
    return text


def remove_unwanted_patterns(text):
    text = remove_garbage(text)
    text = remove_urls_and_emails(text)

    padroes = []
 
    # 14:54 hora_regex
    padroes.append(r'\d{2}:\d{2}(horas)?')

    # ARP15001010 Parecer técnico
    padroes.append(r'ARP\d{4,}')

    # protocolo de ação fiscal FIS-154699
    padroes.append(r'FIS-\d{6}')

    # 10/5-30949876CRM crm_regex
    padroes.append(r'\d{2}/\d+-\d+[cC][rR][mM]')

    # 01-047723/2014 74-000369/2015 74-0001.152/2014 protocolo_e_ano
    padroes.append(r'\d{2}-\d+\.?\d+/\d{4}')

    # 14-007-001.004-5 inscrição fiscal
    padroes.append(r'\d{2}-\d{3}-\d{3}\.\d{3}-\d')

    # telefone
    # 41-9692-5657 (41) 9192-0021
    padroes.append(r'(\()?\d{2}(\))?[- ]\d{4}-\d{4}')

    # 41-99770062
    padroes.append(r'(\()?\d{2}(\))?[- ]\d{4}\d{4}')

    # 3350-9240 
    padroes.append(r'\d{4}-\d{4}')

    # 31/03/2016 01/06/16 28/1/15 31-03-2016 31-03-16 date_regex
    padroes.append(u'\d{2}[/-]\d{2}[/-]\d{2,4}')

    # 14-007-001 dash_numbers_regex
    padroes.append(u'\d{2}-\d{3]-\d{3}')

    # cep_regex
    padroes.append(r'\d{2}\.?\d{3}-\d{3}')

    # 12.527/11 1.135 2651.6617 1980106.300 number_with_dots
    padroes.append(r'\d{1,7}\.\d+(/\d{2})?')

    # SN07113/2015-Q Sanepar
    padroes.append(r'SN\d{2,}/\d+-Q')

    # 3103/2016 23/4 05/08 8112/⁠90 slash_numbers
    padroes.append(u'\d{2,}/\d+')

    # protocol_regex 00034214i
    padroes.append(r'\d{4,11}[iI]')

    # AWH-6092 FSS 2245 AZZ6594 placa_regex
    padroes.append(r'\b\w{3}[ -]?\d{4}[,]?\b')

    # BXF-ALY poste_regex
    padroes.append(r'\b[\w\d]{3}-[\w\d]{3}\b')

    # 2425-5 número de casa.
    padroes.append(u'\d+-\d')

    # Any integer bigger than 999. number_regex
    padroes.append(r'\d{4,}')

    for padrao in padroes:
        text = re.sub(padrao, '', text)

    return text


def build_stop_word_regex(stop_word_file_path):
    stop_word_list = load_stop_words(stop_word_file_path)
    stop_word_regex_list = []

    for word in stop_word_list:
        word_regex = r'\b{}(?![\w-])'.format(word)
        stop_word_regex_list.append(word_regex)

    # Special patterns for my personal problem.
    # The order of the expressions is MANDATORY.
    #  |
    # \ /
    #  '
    # Slash (/) and nº are not working if I put in the stopwords file.
    # I don't want hours, dates and the only number I want is 156.
    # \u2060 is a weird non-ascii char.
    patterns = [
        r'\d{2}:\d{2}(horas)?',  # 14:54
        u'\d+h\u2060?\d{2}m?(?:in)?',  # 16h15 - 16h20m - 16:30min
        '\b[\w\d]{3}-[\w\d]{3}\b',  # BXF-ALY
        u'\d+min',  # 30min
        u'\d{1,2}hr?',  # 16h
        r'\d{2}-\d+/\d{4}',  # 01-047723/2014 74-000369/2015
        r'\d+-\w\d+',  # 275350-w004877829
        u'\d{2,}-\u2060?\d+',  # 3103-2016 960-080 63300-39
        u'\d{2,}/\u2060?\d+',  # 3103/2016 23/4 05/08 8112/⁠90
        u'\d{2}/\u2060\d{2}/\u2060\d{4}',  # '10/\u206002/\u20602014
        u'\b\w+-\u2060\w+\b',  # 'vejo-\u2060me'
        r'nº\d{4,11}i',  # nº000338327i
        u'\u2060+',  # weird non-ascii char.
        u'\u202a+',
        u'\u200e+',
        u'\u202c+',
        u'pergunto-\u2060lhe',  # weird non-ascii char.
        u'surpreendi-\u2060me',
        r'/',  # the slash /
        r'nº\d+',  # nº9 nº99 nº999 nº5555 etc ...
        r'[nN]° ?\d+',  # N° 390
        r'nº',  # nº
        r'\d+º',  # 5º
        u'\d+\u00B0',  # 1°
        r'\d+ª',  # 3ª
        r'\d+m(?:ts)?',  # 80m - 400mts
        r'\d+%',  # 40%
        r'\d+cm',  # 80cm
        r'\d+km/h(?:r)?',  # 80km/h
        r'\d+km',  # 5km
        u'\d+m3',  # 2m3 - 20m3
        r'\d{4,}',  # Any integer bigger than 999.
        '\*+',  # * ** *** **** etc ...
        '\++',  # + ++ +++ ++++ etc ...
        '[-\*]+',  # any sequence of - and *
        u'[-\u2060]+',  # - -- --- ---- etc ...
        '\[',  # [
        '\]',  # ]
        ' {2,}',  # mora than one space.
        '[\r\n]',
        '\$',
        '[%&=$<>“#•{}§°´”]',
        '{}+'.format(chr(127)),
    ]

    stop_word_regex_list.extend(patterns)
    
    for i in stop_word_regex_list:
        try:
            re.compile(i, re.IGNORECASE)
        except:
            print(i)

    stop_word_pattern = re.compile('|'.join(stop_word_regex_list), re.IGNORECASE)
    return stop_word_pattern


def generate_candidate_keywords(sentence_list, stopword_pattern):
    phrase_list = []
    for s in sentence_list:
        tmp = re.sub(stopword_pattern, '|', s.strip())
        phrases = tmp.split("|")
        for phrase in phrases:
            phrase = phrase.strip().lower()
            if phrase != "":
                phrase_list.append(phrase)
    return phrase_list


def calculate_word_scores(phraseList):
    word_frequency = {}
    word_degree = {}
    for phrase in phraseList:
        word_list = separate_words(phrase, 0)
        word_list_length = len(word_list)
        word_list_degree = word_list_length - 1
        #if word_list_degree > 3: word_list_degree = 3 #exp.
        for word in word_list:
            word_frequency.setdefault(word, 0)
            word_frequency[word] += 1
            word_degree.setdefault(word, 0)
            word_degree[word] += word_list_degree  #orig.
            #word_degree[word] += 1/(word_list_length*1.0) #exp.
    for item in word_frequency:
        word_degree[item] = word_degree[item] + word_frequency[item]

    # Calculate Word scores = deg(w)/frew(w)
    word_score = {}
    for item in word_frequency:
        word_score.setdefault(item, 0)
        word_score[item] = word_degree[item] / (word_frequency[item] * 1.0)  #orig.
    #word_score[item] = word_frequency[item]/(word_degree[item] * 1.0) #exp.
    return word_score


def generate_candidate_keyword_scores(phrase_list, word_score):
    keyword_candidates = {}
    for phrase in phrase_list:
        keyword_candidates.setdefault(phrase, 0)
        word_list = separate_words(phrase, 0)

        candidate_score = 0
        for word in word_list:
            candidate_score += word_score[word]
        keyword_candidates[phrase] = candidate_score
    return keyword_candidates


class Rake(object):
    def __init__(self, stop_words_path):
        self.stop_words_path = stop_words_path
        self.__stop_words_pattern = build_stop_word_regex(stop_words_path)

    def run(self, text):
        text = remove_unwanted_patterns(text)

        sentence_list = split_sentences(text)

        phrase_list = generate_candidate_keywords(sentence_list, self.__stop_words_pattern)

        word_scores = calculate_word_scores(phrase_list)

        keyword_candidates = generate_candidate_keyword_scores(phrase_list, word_scores)

        sorted_keywords = sorted(iter(keyword_candidates.items()), key=operator.itemgetter(1), reverse=True)
        return sorted_keywords


def run_test(stoppath):
    text = "Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating sets of solutions for all types of systems are given. These criteria and the corresponding algorithms for constructing a minimal supporting set of solutions can be used in solving all the considered types of systems and systems of mixed types."

    # Split text into sentences
    sentenceList = split_sentences(text)
    stopwordpattern = build_stop_word_regex(stoppath)

    # generate candidate keywords
    phraseList = generate_candidate_keywords(sentenceList, stopwordpattern)

    # calculate individual word scores
    wordscores = calculate_word_scores(phraseList)

    # generate candidate keyword scores
    keywordcandidates = generate_candidate_keyword_scores(phraseList, wordscores)
    if debug: print(keywordcandidates)

    sortedKeywords = sorted(iter(keywordcandidates.items()), key=operator.itemgetter(1), reverse=True)
    if debug: print(sortedKeywords)

    totalKeywords = len(sortedKeywords)
    if debug: print(totalKeywords)
    print(sortedKeywords[0:(totalKeywords // 3)])

    rake = Rake(stoppath)
    keywords = rake.run(text)
    print(keywords)


if __name__ == '__main__':
    if test:
        # Fox stoplist contains "numbers", so it will not find
        # "natural numbers" like in Table 1.1
        # stoppath = "FoxStoplist.txt"
        # SMART stoplist misses some of the lower-scoring keywords
        # in Figure 1.5, which means that the top 1/3 cuts off one
        # of the 4.0 score words in Table 1.1
        # stoppath = "SmartStoplist.txt"
        # Brazilian portuguese StopList
        stoppath = "stoplists/stopwords_alopes.txt"
        run_test(stoppath)
