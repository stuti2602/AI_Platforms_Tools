from text_preprocessing import preprocess_text
from sentiment_analysis import analyze_sentiment_trends
from keyword_detection import detect_keywords
from readability_metrics import calculate_readability

# Sample corpus
corpus = [
    "I love learning Python programming!",
    "Natural Language Processing is a fascinating field.",
    "The weather today is gloomy, which makes me feel sad."
]

# 1. Preprocessing
all_tokens = []
for text in corpus:
    tokens = preprocess_text(text)
    all_tokens.extend(tokens)

print("\nPreprocessed Tokens:", all_tokens)

# 2. Sentiment Analysis
sentiment_df = analyze_sentiment_trends(corpus)
print("\nSentiment Trends:\n", sentiment_df)

# 3. Keyword Detection
keywords = detect_keywords(all_tokens, top_n=5)
print("\nTop Keywords:", keywords)

# 4. Readability Metrics
for idx, text in enumerate(corpus):
    print(f"\n Readability for Text {idx+1}:")
    print(calculate_readability(text))
