# Group 16

# Team members:

# Zenan Ji (Student ID: 1122396) - city: Nanjing

# Weijie Ye (Student ID: 1160818) - city: Fuzhou

# Wenqin Liu (Student ID: 807291) - city: Guangdong

# Jinhong Yong (Student ID: 1198833) - city: Kuala Lumpur

# Zixuan Zeng (Student ID: 1088297) - city: Melbourne

import snownlp
from textblob import TextBlob
import nltk


class SentimentScore():
    '''
    input： whole twitter text
    output: this text sentiment score
    '''
    def __init__(self):
        self.sentences = []

    def socre(self,twitter):
        nltk.download('punkt')
        self.sentences = TextBlob(twitter).sentences
        sentence_score = 0
        for i in range(len(self.sentences)):
            sentence_score += (self.sentences[i].sentiment)[0]

        return sentence_score*100


