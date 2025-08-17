import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

def extract_keywords(df, text_col):
    all_text = " ".join(df[text_col].dropna().astype(str))
    tokens = [t for t in nltk.word_tokenize(all_text.lower())
              if t.isalpha() and t not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    counts = Counter(tokens)
    return counts.most_common(10)
