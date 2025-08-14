# Q-2 Prompt Optimization Framework 
# - Develop a framework that automatically adapts prompts for: 
# - Summarization - Text classification 
# - Creative text generation 
# - The framework should detect the task type and adjust prompt style, length, and structure accordingly

from transformers import pipeline

# Summarization function
def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn",trust_remote_code=True)
    result = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return result[0]['summary_text']

# Text classification function
def classify_text(text):
    classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english",trust_remote_code=True)
    result = classifier(text)
    return f"Label: {result[0]['label']}, Confidence: {result[0]['score']:.4f}"

# Creative text generation function
def generate_text(prompt):
    generator = pipeline("text-generation", model="gpt2",trust_remote_code=True)
    result = generator(prompt, max_length=50, num_return_sequences=1)
    return result[0]['generated_text']


# Main execution starts here
if __name__ == "__main__":
    # Example for summarization
    print("=== Summarization ===")
    print("Loading summarizer model...")
    print(summarize_text("Artificial Intelligence is transforming industries by automating processes and enhancing decision-making. Companies are investing heavily in AI research."))

    # Example for text classification
    print("\n=== Text Classification ===")
    print("\nLoading classifier model...")
    print(classify_text("I really love this new phone!"))

    # Example for creative text generation
    print("\n=== Creative Text Generation ===")
    print("\nLoading generator model...")
    print(generate_text("Once upon a time, there was a magical forest"))
