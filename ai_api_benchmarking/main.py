from benchmark import benchmark_model
from report import print_report

if __name__ == "__main__":
    # Sample dataset
    samples = ["I love AI", "This is bad"]

    # Two models to compare
    model_1 = "distilbert-base-uncased-finetuned-sst-2-english"
    model_2 = "bert-base-uncased"

    # Run benchmarks
    results1, latency1 = benchmark_model(model_1, samples)
    results2, latency2 = benchmark_model(model_2, samples)

    # Print reports
    print_report(model_1, results1, latency1)
    print_report(model_2, results2, latency2)
