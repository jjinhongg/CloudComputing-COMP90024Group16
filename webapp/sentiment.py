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


