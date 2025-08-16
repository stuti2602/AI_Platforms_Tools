from textblob import TextBlob
import pandas as pd

def analyze_sentiment_trends(texts):
    results = []
    for idx, text in enumerate(texts):
        sentiment = TextBlob(text).sentiment.polarity
        results.append({"Text_Index": idx + 1, "Sentiment_Score": sentiment})
    
    return pd.DataFrame(results)
