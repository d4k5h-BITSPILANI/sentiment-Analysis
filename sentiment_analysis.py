from textblob import TextBlob

def analyze_sentiment(text):
    testimonial = TextBlob(text)
    polarity = testimonial.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    text_input = input("Enter a text for sentiment analysis: ")
    sentiment = analyze_sentiment(text_input)
    print(f"The sentiment of the text is: {sentiment}")
