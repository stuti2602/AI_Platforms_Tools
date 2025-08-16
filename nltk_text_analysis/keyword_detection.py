from collections import Counter
import nltk

def detect_keywords(tokens, top_n=5):
    word_freq = Counter(tokens)
    return word_freq.most_common(top_n)
