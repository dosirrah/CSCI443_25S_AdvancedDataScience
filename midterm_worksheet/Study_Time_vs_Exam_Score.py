import numpy as np
import matplotlib.pyplot as plt

# For reproducibility
np.random.seed(42)

# Number of data points
n = 200

# Generate study time (in hours) uniformly between 0 and 10
study_time = np.random.uniform(0, 10, n)

# Generate exam scores with diminishing returns:
# A saturating exponential function plus noise
# Base formula: score = 30 + 70*(1 - exp(-0.4 * study_time))
# Then add random normal noise
noise = np.random.normal(loc=0, scale=3, size=n)
exam_scores = 30 + 70 * (1 - np.exp(-0.4 * study_time)) + noise

# Clip exam scores to the range [0, 100] just to ensure no unrealistic values
exam_scores = np.clip(exam_scores, 0, 100)

# Create scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(study_time, exam_scores, c='blue', alpha=0.6, edgecolors='black')
plt.title('Study Time vs. Exam Score (Diminishing Returns)')
plt.xlabel('Study Time (hours)')
plt.ylabel('Exam Score')
plt.grid(True, alpha=0.3)

# Save plot as a PNG
plt.savefig("Study_Time_vs_Exam_Score.png", dpi=300, bbox_inches='tight')
plt.close()

print("Scatter plot saved to Study_Time_vs_Exam_Score.png")




