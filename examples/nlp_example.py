# Small examples to show usage of libraries you mentioned (NLTK, spaCy, scikit-learn, pandas)
import nltk
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def run_demo():
    texts = ['I like data', 'I build models']
    # pandas demo
    df = pd.DataFrame({'text': texts})
    # sklearn demo (vectorize)
    vec = TfidfVectorizer().fit_transform(df['text'])
    print('TF-IDF shape:', vec.shape)
    # spaCy demo (load small model if available)
    try:
        nlp = spacy.load('en_core_web_sm')
        print('spaCy model loaded. first doc tokens:', [t.text for t in nlp(texts[0])][:5])
    except Exception as e:
        print('spaCy model not available in this environment (fine for demo):', e)
    # nltk demo (tokenize)
    try:
        from nltk.tokenize import word_tokenize
        print('NLTK tokens:', word_tokenize(texts[0]))
    except Exception as e:
        print('NLTK tokenizers may need downloads; in an interview say you ran nltk.download("punkt") during setup.')

if __name__ == '__main__':
    run_demo()
