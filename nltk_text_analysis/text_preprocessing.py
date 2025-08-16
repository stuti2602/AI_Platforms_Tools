# Q-5 NLTK-Based Text Analysis System 
# Develop a script that: 
# - Preprocesses a corpus (tokenization, stopword removal, lemmatization) 
# - Analyzes sentiment trends over time 
# - Detects frequently occurring topics or keywords 
# - Calculates basic readability metrics 


import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    # Tokenize text
    tokens = nltk.word_tokenize(text.lower())

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]

    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return tokens
