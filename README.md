<<<<<<< HEAD
x# Classification Evaluation Metrics Playground

## Overview
This project demonstrates how different evaluation metrics behave in a binary classification problem. It highlights why accuracy alone can be misleading.

---

## Metrics Implemented
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Key Insight
Different problems require different metrics:

- Spam detection → Recall is important (catch all spam)
- Fraud detection → Precision is important (avoid false alarms)

---

## Confusion Matrix

TP: correctly predicted positive  
TN: correctly predicted negative  
FP: incorrectly predicted positive  
FN: missed positive  

---

## Visualization
The project plots all metrics side-by-side to compare performance.

---

## How to Run

```bash
pip install -r requirements.txt
python main.py
=======
# classification-model-diagnostic-simulator
Implements core classification evaluation metrics from scratch, including confusion matrix, accuracy, precision, recall, and F1-score. Demonstrates how different prediction errors impact each metric and why accuracy alone can be misleading. Includes simple visualizations to compare performance.
>>>>>>> 49e14f7e7f5e32fa3250a35f46bd89afc2f0ec5c
