# Q-1 1. Hugging Face Model Integration Script 
# Write a Python script that: 
# - Loads a Hugging Face model and tokenizer 
# - Performs inference on sample input 
# - Includes robust error handling and logging 
# - Demonstrates performance optimization (batching, GPU usage if available)

from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch


def hugging_face_model_run():

    # Choose a ready-made model from Hugging Face Hub
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"

    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    # Check if GPU is available (for faster performance)
    device = 0 if torch.cuda.is_available() else -1

    # Create a pipeline for sentiment analysis
    nlp_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, device=device)

    # Sample text input (batched for performance)
    texts = [
        #"I love using Hugging Face models!",
        #"This is the worst day ever."
        "Am i Good Girl?",
        "AI will replace the human."
    ]

    # 6. Run inference (prediction)
    results = nlp_pipeline(texts)

    # 7. Show results
    for text, result in zip(texts, results):
        print(f"Text: {text}")
        print(f"Prediction: {result['label']}")
        print(f"Confidence Score: {result['score']:.4f}")
        print("-" * 40)


if __name__ == "__main__":
    hugging_face_model_run()