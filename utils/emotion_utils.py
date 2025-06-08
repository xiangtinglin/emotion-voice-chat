from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import os

def analyze_sentiment(text):
    client = TextAnalyticsClient(
        endpoint=os.environ["TEXT_ENDPOINT"],
        credential=AzureKeyCredential(os.environ["TEXT_KEY"])
    )
    result = client.analyze_sentiment(documents=[text])[0]
    return result.sentiment

