#!/usr/bin/env python3

import tika
from tika import parser

import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize

# from stop_words import get_stop_words
from nltk.corpus import stopwords



from papervis.bibparser import BibParser

from sklearn.feature_extraction.text import TfidfVectorizer

import yaml
import os
import string
import json

config = yaml.safe_load(open("config/config.yml"))

class StemmerSimilarity:
    def __init__(self):
#        nltk.download('punkt') # if necessary...
#        nltk.download('stopwords')
        self.stemmer = nltk.stem.porter.PorterStemmer()
        self.remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
        self.vectorizer = TfidfVectorizer(tokenizer = self.normalize, stop_words = 'english')


    def stem_tokens(self,tokens):
        return [self.stemmer.stem(item) for item in tokens]

    '''remove punctuation, lowercase, stem'''
    def normalize(self,text):
        return self.stem_tokens(nltk.word_tokenize(text.lower().translate(self.remove_punctuation_map)))
        
    def process(self,text):
        return self.stem_tokens(self.normalize(text))
        
    def remove_stopwords(self,word_list):
        return [word for word in word_list if word not in stopwords.words('english')]

    def get(self,data):
        tfidf = self.vectorizer.fit_transform([data['a'], data['b']])
        return ((tfidf * tfidf.T).A)[0,1]

def parse_pdf_to_raw(pdf_file_path):
    """converts pdf file to raw and returns contents"""
    raw = parser.from_file(pdf_file_path)
    return raw #['content']

def main ():
    """"""
    bp = BibParser()
    
    # open index bibtex file
    bp.open(config['path'])
    
    # prefix path from bibtext file
    prefix_path = os.path.dirname(os.path.realpath(config['path']))
    
    word_stems_all = dict()
    freq_all = dict()
    
    # get all pdf names
    for identifier in bp.pdf_files:
        # print(bp.pdf_files[identifier])
        file_name = prefix_path + os.path.sep + bp.pdf_files[identifier]
        data = parse_pdf_to_raw(file_name)
        
        # stem words
        ss = StemmerSimilarity()
        word_stems = ss.process(data['content'])
        
        # remove stop words
        word_stems = ss.remove_stopwords(word_stems)
        
        # merge data over id
        word_stems_all[identifier] = word_stems
        
        # frequencies
        fdist = nltk.FreqDist(word_stems)

        # merge all frequencies
        freq_all[identifier] = [] 
        
        for word,freq in fdist.most_common(50):
            freq_all[identifier].append( {'word' : word, 'size' : freq } )
        
        # break
    
    words_all = []
    for key,words in word_stems_all.items():
        words_all += words
        
    # print(words_all)
    
    # for ident, words in word_stems_all[0]:
        # words_all.append(words)
    #
    # frequencies
    fdist_all = nltk.FreqDist(words_all)
    
    # print(fdist_all)
    

    freq_all_merged = []
    for word,freq in fdist_all.most_common(50):
        freq_all_merged.append( {'word' : word, 'size' : freq } )

    
    # print(fdist_all)
    json_freq = json.dumps({'input' : freq_all_merged})
    
    # per paper frequency 
    # print(json_freq)
    
    

if __name__  == "__main__":
    main()
