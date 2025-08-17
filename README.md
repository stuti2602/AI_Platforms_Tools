# AI_Platforms_Tools

# Problem_1: Hugging Face Model Integration Script

- Purpose: Load a pre-trained Hugging Face model, perform inference, handle errors, and optimize performance.

- Hugging Face model URL: https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english

- How to run: pip install -r requirements.txt 
              python hugging_face_model_integration_script.py

- Explanation: Uses transformers library
               Demonstrates tokenization, model inference, batching

- Example: sentiment analysis on sample text


| Task Type               | What it Does                       | Example Hugging Face Model                        | Example Output   |
| ----------------------- | ---------------------------------- | ------------------------------------------------- | ---------------- |
| **Sentiment Analysis**  | Finds if text is positive/negative | `distilbert-base-uncased-finetuned-sst-2-english` | "Positive"       |
| **Text Classification** | Classifies text into topics        | `facebook/bart-large-mnli`                        | "Sports"         |
| **Translation**         | Translates between languages       | `Helsinki-NLP/opus-mt-en-fr`                      | English → French |
| **Question Answering**  | Finds answer from a paragraph      | `distilbert-base-cased-distilled-squad`           | "New Delhi"      |



# problem_2: Prompt Optimization Framework

- Purpose: Detect task type (summarization, classification, generation) and adapt prompts automatically.

- Hugging Face summarization Model URL : https://huggingface.co/facebook/bart-large-cnn
  Hugging Face text classification Model URL : https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english
  Hugging Face creative text generation Model URL : https://huggingface.co/gpt2

- How to run :  pip install -r requirements.txt
                prompt_optimization_framwork.py

- Key Concepts: Task detection
                Prompt modification based on task
                Simple example of summarization or text classification


| Task Type                       | Model Name                                        | Why Chosen                                       |
| ------------------------------- | ------------------------------------------------- | ------------------------------------------------ |
| Summarization                   | `facebook/bart-large-cnn`                         | Pre-trained on CNN/DailyMail news dataset,       |
|                                 |                                                   | good for short, clean summaries. Well-tested and |
|                                 |                                                   |  widel used.                                     |
| Text Classification (Sentiment) | `distilbert-base-uncased-finetuned-sst-2-english` | Small, fast, and accurate mode for binary        |
|                                 |                                                   | classification (positive/negative). Easy to      |
|                                 |                                                   | explain.                                         |
| Creative Text Generation        | `gpt2`                                            | Popular open-source model for creative writing.  |


# problem_3: Automated Data Exploration with pandas

- Purpose: Automatically explore datasets:
           Generate column summaries
           Detect missing values, duplicates, outliers
           Recommend preprocessing steps
           Output structured report

How to run: pip install -r requirements.txt
            python automated_data_exploration.py


# problem_4: Multi-Panel Visualization Dashboard

- Purpose: Supports different data types
           Automatically selects chart types
           Displays multiple panels for comparison
           Includes legends, titles, annotations

- Libraries: matplotlib, seaborn

- How to run: pip install -r requirements.txt
              python multi_panel_dashboard.py


# problem:5 : NLTK-Based Text Analysis System


nltk_text_analysis/
│
├── text_preprocessing.py   # Handles tokenization, stopword removal, lemmatization
├── sentiment_analysis.py   # Performs sentiment trend analysis
├── keyword_detection.py    # Detects frequent words/topics
├── readability_metrics.py  # Calculates readability scores
└── main.py                  # Main script that ties everything together

1) text_preprocessing.py

- Purpose: Clean and preprocess text data

- Functions: Tokenization → Splits text into words
             Stopword removal → Removes common words like “the”, “is”
             Lemmatization → Reduces words to their root form

- Example: Converts "running happily" → ["run", "happily"]

2) sentiment_analysis.py

- Purpose: Analyze sentiment trends in text

- Functionality: Classifies text as positive, negative, or neutral
                 Generates simple summary statistics

- Example Output: Text: "I love AI!" → Sentiment: POSITIVE
                  Text: "This is bad." → Sentiment: NEGATIVE


3) keyword_detection.py

- Purpose: Detect frequently occurring words or topics

- Functionality: Counts word frequency
                 Ignores stopwords ("the," "and," "is," and "a,")
                 Provides top N keywords for the dataset


4) readability_metrics.py

- Purpose: Calculate basic readability metrics

- Functionality: Measures text complexity (e.g., average word length, sentence length)
                 Provides a readability score to assess text difficulty

5) main.py

- Purpose: Ties all modules together for execution

- Functionality: Loads dataset
                 Calls preprocessing → sentiment → keyword → readability
                 Displays summarized results

- How to run: pip install -r requirements.txt
              python main.py


- Key Features : Tokenization, stopword removal, lemmatization
                 Sentiment trend analysis
                 Detection of frequently occurring words/topics
                 Readability metrics calculation
                 Modular design for clarity and maintainability


# problem: 6 pandas Data Transformation Pipeline

pandas_pipeline/
│── pipeline.py          # Main class with all transformations
│── utils.py             # Helper functions (outliers, scaling, etc.)
│── main.py              # Example usage / Run this file

1) pipeline.py

- Purpose: Implements the main transformation class

- Functions: Handle missing values
             Detect & remove outliers
             Apply scaling (MinMax, StandardScaler)

- Example: 
          from pipeline import DataPipeline
          pipeline = DataPipeline()
          df_clean = pipeline.run(df)

2) utils.py

- Purpose: Helper functions for pipeline operations

- Functions: Outlier detection using IQR
             Scaling functions (min-max, z-score)
             Logging steps for debugging and clarity

3) main.py

- Purpose: Example usage and entry point for the pipeline

- Functionality: Loads sample dataset
                 Initializes pipeline
                 Runs all transformations and prints results

- How to run: pip install -r requirements.txt
              python main.py



- Key Features: Handle missing values (mean, median, mode, or drop)
                Detect and remove outliers
                Perform feature scaling (normalization, standardization)
                Log each transformation step
                Modular design for easy understanding


# problem: 7 Visualization Automation Tool 

visualization_tool/
│── data_loader.py
│── eda_report.py
│── run_visualization.py

1) data_loader.py

- Purpose: Load dataset for analysis

- Functionality: Reads CSV or Excel files (Titanic Dataset)
                 Checks for missing values
                 Returns pandas DataFrame for further processing

2) eda_report.py

- Purpose: Generate EDA visualizations and summary statistics

- Functionality: Detects numeric vs categorical columns
                 Creates visualizations:
                    Numeric → histograms, boxplots
                    Categorical → barplots
                 Generates descriptive statistics (mean, median, mode, etc.)

3) run_visualization.py

- Purpose: Main entry point to run the visualization tool

- Functionality: Loads dataset using data_loader.py
                 Calls eda_report.py to generate visualizations and statistics
                 Displays/save visualizations


- How to run: pip install -r requirements.txt
              python run_visualization.py

- Key Features: Accepts any dataset (CSV/Excel)
                Automatically detects numeric and categorical columns
                Generates suitable visualizations (histograms, barplots, boxplots)
                Provides summary statistics for each column
                Modular and reusable design
                
# problem: 8 AI API Performance Benchmarking


ai_api_benchmarking/
├── benchmark.py   # main benchmarking logic
├── main.py        # entry point to run the benchmarking


1) benchmark.py

- Purpose: Implements the core benchmarking logic

- Functionality: Sends requests to multiple AI APIs
                 Records response time (latency)
                 Calculates throughput (requests per second)
                 Optionally evaluates accuracy if reference output is provided

2) main.py

- Purpose: Entry point to run the benchmark

- Functionality: Imports benchmark.py
                 Loads sample input data
                 Runs API benchmarking
                 Displays or saves results as a report


- How to run: pip install -r requirements.txt
              python run_visualization.py

- Key Features: Compare at least 2 AI APIs on the same inputs
                Measure latency (response time) and throughput (requests per second)
                Evaluate prediction accuracy
                Logs and reports performance metrics
                Modular design for easy understanding




# project_C: Major Project – Intelligent Data Analysis Assistant 

intelligent_data_assistant_simple/
│
├── app.py                 # Main Streamlit app
├── data_processing.py     # Data cleaning & numeric/text summaries
├── visualization.py       # Plot functions
├── nlp_module.py          # NLTK keyword extraction
├── ai_integration.py      # Hugging Face sentiment / fallback
├── report_generator.py    # Simple report generation


- overview : The Intelligent Data Assistant is a Streamlit-based data analysis tool that helps users quickly analyze datasets           
             without needing advanced programming knowledge.
             It combines data processing, visualization, NLP, and AI-powered insights in one easy-to-use web application.
             This project demonstrates how to build an interactive AI-powered analytics assistant that supports:
                    Dataset upload & preprocessing
                    Automatic data summary and cleaning
                    Visualizations (charts & graphs)
                    Text analysis (NLP with NLTK)
                    AI-powered sentiment analysis (via Hugging Face)
                    Simple PDF report generation

- Features :
        Streamlit Web App – clean UI to upload data and explore it interactively.
        Data Preprocessing – missing values handling, numeric/categorical summaries.
        Visualizations – histograms, boxplots, scatterplots, correlation heatmaps.
        NLP Analysis – keyword extraction & basic text insights.
        AI Integration – Hugging Face API for sentiment analysis, fallback local models.
        Report Generation – export results and visualizations into PDF.
        Extensible – easy to extend with more AI/ML models.

1) data_processing.py

- Cleans dataset (missing values, type detection).
- Provides summary statistics for numeric & categorical columns.

2) visualization.py

- Uses Matplotlib & Seaborn.
- Supports histograms, scatterplots, bar charts, and heatmaps.

3) nlp_module.py

-Tokenizes text, removes stopwords.
- Extracts keywords and frequent terms.

4) ai_integration.py

- Connects with Hugging Face models (e.g., sentiment-analysis).
- Supports fallback rule-based methods if API unavailable.

5) report_generator.py

- Creates a PDF report with:
- Data summary
- Visualizations
- NLP insights
- AI-powered sentiment analysis

6) app.py

- Main Streamlit frontend.
- Connects all modules → users interact here.

- How to run: pip install -r requirements.txt
              streamlit run app.py