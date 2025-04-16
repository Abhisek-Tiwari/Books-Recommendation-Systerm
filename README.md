
# Books Recommendation System

**Trained on 7,000 books, this Large Language Model (LLM) recommends books based on user prompts via a Gradio interface.**

## Overview

This project leverages machine learning and natural language processing techniques to provide personalized book recommendations. By analyzing a curated dataset of 7,000 books, the system can suggest titles that align with user preferences and inputs.

## Features

- **Interactive Gradio UI**: Engage with the recommendation system through a user-friendly web interface.
- **Comprehensive Dataset**: Utilizes a rich dataset containing book titles, categories, descriptions, and emotional tones.
- **Advanced NLP Techniques**: Incorporates sentiment analysis and vector-based search to enhance recommendation accuracy.

## Dataset

The system is built upon a dataset comprising 7,000 books, each annotated with metadata such as:

- **book_cleaned.csv**: Contains cleaned book titles and relevant information.
- **book_with_category.csv**: Includes book titles along with their respective categories.
- **books_with_emotion.csv**: Features books tagged with emotional descriptors to capture the tone and mood.

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Abhisek-Tiwari/Books-Recommendation-Systerm.git
   cd Books-Recommendation-Systerm
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   *Note: Ensure that `requirements.txt` is present in the repository. If not, manually install the necessary packages such as `gradio`, `pandas`, `numpy`, etc.*

## Usage

To launch the Gradio interface and start receiving book recommendations:

```bash
python gradio-dashboard.py
```

Once executed, a local web server will start, and you'll receive a URL (typically `http://127.0.0.1:7860/`) to access the interface in your browser.

## Project Structure

- **gradio-dashboard.py**: Main script to launch the Gradio web interface.
- **data_preprocessing.ipynb**: Jupyter notebook detailing the data cleaning and preprocessing steps.
- **sentiment_analysis.ipynb**: Notebook focusing on sentiment analysis of book descriptions.
- **vector-search.ipynb**: Implements vector-based search mechanisms for recommendations.
- **tagged_description.txt**: Contains book descriptions tagged with relevant metadata.
- **cover-not-found.jpg**: Placeholder image for books without available cover images.

## Contributing

Contributions are welcome! If you'd like to enhance the system, fix bugs, or add new features, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeatureName
   ```
5. Open a pull request detailing your changes.


## 📬 Connect with Me

- **GitHub:** [Abhisek-Tiwari](https://github.com/Abhisek-Tiwari)
- **LinkedIn:** [abhisek-tiwari-a06315262](https://www.linkedin.com/in/abhisek-tiwari-a06315262/)


⭐️ If you like this project, don't forget to leave a star!
