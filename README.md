## How to Run
# Classification Evaluation Metrics Playground

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