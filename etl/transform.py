import os
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob

# Download stopwords (only needed once)
nltk.download('stopwords')

def transform_headlines(df):
    STOPWORDS = set(stopwords.words('english'))

    def clean_text(text):
        text = re.sub(r'[^a-zA-Z ]', '', str(text))
        text = text.lower()
        text = ' '.join(word for word in text.split() if word not in STOPWORDS)
        return text

    df['clean_title'] = df['title'].apply(clean_text)
    df['sentiment'] = df['clean_title'].apply(lambda x: TextBlob(x).sentiment.polarity)

    def label_sentiment(score):
        if score > 0.1:
            return 'Positive'
        elif score < -0.1:
            return 'Negative'
        else:
            return 'Neutral'

    df['sentiment_label'] = df['sentiment'].apply(label_sentiment)

    # ✅ Save transformed data (simplified)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/headlines_transformed.csv", index=False)
    print("✅ Transformed data saved to data/headlines_transformed.csv")

    return df
