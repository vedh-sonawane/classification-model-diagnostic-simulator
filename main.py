import numpy as np
import matplotlib.pyplot as plt
from metrics import *

# Example: binary classification (0 = not spam, 1 = spam)
y_true = np.array([1,0,1,1,0,1,0,0,1,0])

# Simulate predictions (you will tweak this)
y_pred = np.array([1,0,1,0,0,1,1,0,1,0])

tp, tn, fp, fn = confusion_matrix(y_true, y_pred)

acc = accuracy(tp, tn, fp, fn)
prec = precision(tp, fp)
rec = recall(tp, fn)
f1 = f1_score(prec, rec)

print("Confusion Matrix:")
print(f"TP: {tp}, TN: {tn}, FP: {fp}, FN: {fn}\n")

print(f"Accuracy:  {acc:.2f}")
print(f"Precision: {prec:.2f}")
print(f"Recall:    {rec:.2f}")
print(f"F1 Score:  {f1:.2f}")

# Simple bar chart
labels = ["Accuracy", "Precision", "Recall", "F1"]
values = [acc, prec, rec, f1]

plt.bar(labels, values)
plt.ylim(0, 1)
plt.title("Evaluation Metrics Comparison")
plt.show()