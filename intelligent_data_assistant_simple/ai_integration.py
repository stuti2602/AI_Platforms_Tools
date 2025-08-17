from transformers import pipeline

def get_sentiment(df, text_col):
    try:
        pipe = pipeline("sentiment-analysis")
        sample_texts = df[text_col].dropna().astype(str).head(5).tolist()
        return pipe(sample_texts)
    except:
        # Simple fallback
        def simple_sentiment(text):
            pos = sum(word in text.lower() for word in ["good","great","happy","love"])
            neg = sum(word in text.lower() for word in ["bad","sad","hate","worst"])
            if pos>neg: return "POSITIVE"
            elif neg>pos: return "NEGATIVE"
            else: return "NEUTRAL"
        return [simple_sentiment(t) for t in df[text_col].head(5)]
