
import numpy as np
import matplotlib.pyplot as plt

# For reproducibility
np.random.seed(42)

# Generate a normal distribution around mean=80, sd=12
scores = np.random.normal(loc=80, scale=12, size=1000)

# Clip the upper tail at 100
scores_clipped = np.clip(scores, a_min=None, a_max=100)

# Compute mean and median after clipping
mean_score = np.mean(scores_clipped)
median_score = np.median(scores_clipped)

# Print to console (optional)
print("Mean (Clipped):", mean_score)
print("Median (Clipped):", median_score)

# Plot the histogram
plt.figure(figsize=(8, 5))
plt.hist(scores_clipped, bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of Exam Scores (Clipped at 100)')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)

# Save the figure
plt.savefig("Exam_Scores_Histogram.png", dpi=300, bbox_inches='tight')
plt.close()

#plt.show()

