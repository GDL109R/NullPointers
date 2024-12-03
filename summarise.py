import os

# This example requires environment variables named "LANGUAGE_KEY" and "LANGUAGE_ENDPOINT"
key = "CdyrFJGcwalz8miGY1EmnhI3Sn1dkQ4f1bvelJE7lUbAoTWx8osaJQQJ99ALACmepeSXJ3w3AAAAACOGAt3k"
endpoint = "https://ai-nullpointerai437316831927.openai.azure.com/"

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Authenticate the client using your key and endpoint 
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

# Example method for summarizing text
def sample_extractive_summarization(client, text):
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import (
        TextAnalyticsClient,
        ExtractiveSummaryAction
    ) 

    document = [
        text
    ]

    poller = client.begin_analyze_actions(
        document,
        actions=[
            ExtractiveSummaryAction(max_sentence_count=4)
        ],
    )

    document_results = poller.result()
    for result in document_results:
        extract_summary_result = result[0]  # first document, first result
        if extract_summary_result.is_error:
            print("...Is an error with code '{}' and message '{}'".format(
                extract_summary_result.code, extract_summary_result.message
            ))
        else:
            print("Summary extracted: \n{}".format(
                " ".join([sentence.text for sentence in extract_summary_result.sentences]))
            )

def extract(text):
    sample_extractive_summarization(client, text)