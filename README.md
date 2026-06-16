# AI Text Similarity Detection System

## Overview

AI Text Similarity Detection System is a Natural Language Processing (NLP) based web application that compares two text inputs and calculates their similarity percentage. The system uses TF-IDF Vectorization and Cosine Similarity algorithms to analyze textual content and determine how closely two texts are related.

Additionally, the application compares user input with a large dataset and identifies the highest similarity score from the dataset.

---

## Features

✅ Compare two text inputs

✅ Calculate similarity percentage

✅ Dataset-based similarity comparison

✅ Modern AI-inspired user interface

✅ Real-time text analysis

✅ Fast and efficient NLP processing

---

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Pandas
- Scikit-learn
- Natural Language Processing (NLP)

---

## Algorithms Used

### TF-IDF (Term Frequency – Inverse Document Frequency)

TF-IDF converts textual data into numerical vectors and identifies important words within a document.

### Cosine Similarity

Cosine Similarity measures the similarity between two text vectors by calculating the cosine of the angle between them.

---

## System Workflow

```text
User Input
    ↓
Text Preprocessing
    ↓
TF-IDF Vectorization
    ↓
Cosine Similarity Calculation
    ↓
Similarity Percentage Generation
    ↓
Result Display
```

---

## Project Structure

```text
AI-Text-Similarity-Detector
│
├── app.py
├── dataset_large.csv
├── requirements.txt
├── README.md
│
├── templates
│   └── index.html
│
└── screenshots
    ├── homepage.png
    └── result.png
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Text-Similarity-Detector.git
```

Move to project folder:

```bash
cd AI-Text-Similarity-Detector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## Example Input

### Text 1

```text
Machine learning is amazing
```

### Text 2

```text
AI and machine learning are powerful
```

### Output

```text
Similarity Score: 26%
Dataset Similarity: 100%
```

---

## Applications

- Plagiarism Detection
- Document Comparison
- Content Similarity Analysis
- Search Engines
- Chatbots
- Educational Platforms
- Research Document Analysis

---

## Future Enhancements

- BERT Semantic Similarity
- AI-Based Text Understanding
- Multi-Document Comparison
- Plagiarism Detection Module
- Similarity Heatmap Visualization
- Advanced NLP Techniques

---

## Learning Outcomes

Through this project:

- Learned Natural Language Processing concepts
- Implemented TF-IDF Vectorization
- Implemented Cosine Similarity
- Developed Flask-based web applications
- Worked with datasets and text analytics
- Built an end-to-end AI project

---

## Author

**Tanmayi K**



--# License

This project is developed for educational and learning purposes.
