def print_report(model_name, results, latency):
    print(f"\n--- Report for {model_name} ---")
    print(f"Latency: {latency:.4f} seconds")
    print("Sample predictions:")
    for text, res in zip(["I love AI", "This is bad"], results):
        print(f"Text: {text} --> Prediction: {res}")
    print("---------------------------")
