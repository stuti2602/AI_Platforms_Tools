import time
from transformers import pipeline

def benchmark_model(model_name, samples):
    # Load model
    nlp = pipeline("sentiment-analysis", model=model_name)

    # Measure start time
    start_time = time.time()

    # Run inference
    results = nlp(samples)

    # Measure end time
    end_time = time.time()

    # Calculate latency
    latency = end_time - start_time

    return results, latency
