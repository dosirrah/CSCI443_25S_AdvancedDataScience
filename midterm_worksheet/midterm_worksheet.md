---
header-includes:
  - "\\usepackage{amsmath}"
  - "\\usepackage{graphicx}"
  - "\\usepackage{unicode-math}"
---


<!--
To compile this into a pdf file use pandoc:

    pandoc midterm_worksheet.md -o midterm_worksheet.pdf --pdf-engine=xelatex
-->


# Midterm Review Worksheet

## CSCI 443: Advanced Data Science

## Spring 2025

This worksheet serves as a review of key midterm topics, including
data types, statistics, correlation, Spark concepts, and practical
data science computations.

### Section 1: Data Types and Basic Statistics

1. Movie ratings (e.g., Excellent, Good, Fair, Poor)
   - (A) Nominal
   - (B) Ordinal
   - (C) Discrete
   - (D) Continuous

\hspace{0.1in}

2. Temperature in degrees Fahrenheit
   - (A) Nominal
   - (B) Ordinal
   - (C) Discrete
   - (D) Continuous

\hspace{0.1in}

3. The number of books borrowed from a library
   - (A) Nominal
   - (B) Ordinal
   - (C) Discrete
   - (D) Continuous

\hspace{0.1in}

4. Types of beverages available at a café (Coffee, Tea, Juice)
   - (A) Nominal
   - (B) Ordinal
   - (C) Discrete
   - (D) Continuous

\hspace{0.1in}

5. The ranking of candidates in an election
   - (A) Nominal
   - (B) Ordinal
   - (C) Discrete
   - (D) Continuous

\newpage

### Section 2: True / False (Circle One)

6. A sample space contains all possible outcomes of a random experiment.
   - (A) True
   - (B) False

\hspace{0.1in}

7. The standard deviation is never negative.
   - (A) True
   - (B) False

\hspace{0.1in}

8. The Pearson correlation coefficient measures causality between two variables.
   - (A) True
   - (B) False

\hspace{0.1in}

9. A Z-score represents how many standard deviations a data point is from the mean.
   - (A) True
   - (B) False

\hspace{0.1in}

10. If two variables have zero correlation, they must be independent.
   - (A) True
   - (B) False

\newpage

### Section 3: Data Distributions and Summary Statistics

Use the histogram below to answer the questions:

![Histogram of Exam Scores](Exam_Scores_Histogram.png){width=90%}

11. What type of distribution does this resemble?
   - (A) Gaussian
   - (B) Uniform
   - (C) Exponential
   - (D) Clipped Gaussian

12. Does this distribution exhibit skew?
   - (A) Left skew
   - (B) Right skew
   - (C) No skew

13. What is the approximate range of exam scores?
   - (A) 0-50
   - (B) 50-75
   - (C) 40-100
   - (D) 0-100

14. If the mean exam score is 80, would the median likely be higher, lower, or the same?
   - (A) Higher
   - (B) Lower
   - (C) Same

15. If the variance is high, what does this tell us about exam score fluctuations?
   - (A) Scores are tightly clustered around the mean
   - (B) Scores are widely spread out
   - (C) There is no variance in the dataset
   - (D) The dataset is categorical

\newpage

### Section 4: Correlation and Relationships Between Variables

Use the scatter plot below to answer the questions:

![Scatter Plot: Study Time vs. Exam Score](Study_Time_vs_Exam_Score.png){width=90%}

16. What general trend is observed between study time and exam scores?
   - (A) Scores increase with study time
   - (B) Scores decrease with study time
   - (C) No correlation

17. What best describes the Pearson correlation coefficient?
   - (A) Positive
   - (B) Negative
   - (C) Near Zero

18. If the correlation coefficient is 0.85, what does this imply?
   - (A) Strong positive relationship
   - (B) Weak negative relationship
   - (C) No correlation

19. Why might exam scores plateau despite increased study time?

  - (A) Diminishing returns at high study durations, so incremental improvements become smaller
  - (B) Randomness in test difficulty
  - (C) Exam scores are normally distributed


20. How would adding sleep hours as a variable affect the analysis?

   - (A) It might improve predictive accuracy if sleep is correlated with exam performance.
   - (B) It would have no net effect, because sleep hours are typically uncorrelated with scores.
   - (C) It could create bias by introducing confounding factors related to study time.


\newpage

### Section 5: Spark and Data Engineering

21. Which of the following is a key advantage of using Apache Spark over a local solution with Pandas or NumPy?

- (A) Spark automatically scales computations across a cluster, handling datasets larger than a single machine’s memory.
- (B) Spark is always faster, even for small datasets with minimal computations.
- (C) Spark never processes data in memory, eliminating out-of-memory errors.
- (D) Spark only works with Python, making it simpler to integrate into existing Python code.


22. Which of the following statements best describes the difference between `pyspark.pandas` and Spark DataFrames?

   - (A) `pyspark.pandas` always runs faster because it fully bypasses the Spark engine, whereas Spark DataFrames process everything row by row.  
   - (B) Spark DataFrames can evaluate transformations in a more globally optimized manner, while `pyspark.pandas` offers a Pandas-like interface that may not always produce the same efficiency in multi-step workflows.  
   - (C) `pyspark.pandas` is just a thin wrapper over Spark DataFrames, giving identical performance and query plans.  
   - (D) Spark DataFrames are restricted to Scala, whereas `pyspark.pandas` works only with Python in local mode.


23. What is the difference between Spark DataFrames and RDDs?
   - (A) DataFrames are optimized for queries, RDDs are lower-level
   - (B) RDDs are faster than DataFrames
   - (C) DataFrames do not support distributed computing

24. What does **lazy evaluation** mean in Spark?
   - (A) Operations are only computed when an action is triggered
   - (B) Spark executes transformations immediately
   - (C) Spark delays computations indefinitely

25. How does **shuffling** impact Spark job performance?
   - (A) It can slow down performance due to data movement
   - (B) It speeds up execution
   - (C) It eliminates the need for data partitioning

---

### Section 6: Sampling Distributions, Z-Scores, and Confidence Intervals

**Multiple Choice**

26. Which of the following best describes a **sampling distribution**?

- (A) The distribution of the raw data from a single sample of size *N*.
- (B) The distribution of a statistic (e.g., the mean) computed from many random samples each of size *N* drawn from the same population.
- (C) The distribution that arises from repeatedly partitioning one sample into smaller subsets.
- (D) The distribution of the entire population from which the sample is drawn.


27. Which of the following best describes a **confidence interval**?

- (A) If we repeatedly take samples and build confidence intervals each time, about 95% of those intervals will contain the true parameter.
- (B) The exact range of data points collected in the sample.
- (C) A fixed interval determined by the median only.
- (D) The probability is 95% that the true parameter lies within this specific computed interval.

28. Under which condition is it **appropriate to use a t-distribution** instead of a normal distribution?
   - (A) The sample size is very large (n > 1000).
   - (B) The population variance is known exactly.
   - (C) The sample size is small and the population standard deviation is unknown.
   - (D) The dataset is nominal.

\newpage

**Short Answer: Show Your Work**

29. **Percentiles**  
   Suppose you have a data set of exam scores: 65, 70, 72, 78, 80, 85, 90, 95.  
   **Find the 75th percentile** using linear interpolation if needed.

```















```

30. **Z-Score Calculation**  
   A population of exam scores is approximately normal with mean \\(\\mu = 80\\) and standard deviation \\(\\sigma = 5\\).  
   **What is the Z-score** for a student who scores 90 on the exam?

\newpage


31. **Confidence Interval (Large n)**  
   You collect a sample of **n=100** exam scores, with a sample mean \\(\\overline{x} = 78\\) and **known** population standard deviation \\(\\sigma = 8\\).  
   Construct a **95% confidence interval** for the population mean.  
   (Use the Z-interval since n is large and \\(\\sigma\\) is known. See the table on the next page)

```











```

32. **Confidence Interval (Small n)**  
   Now consider a smaller sample, **n=15**, with a sample mean of 78 and a **sample standard deviation** of 8.  
   Construct a **95% confidence interval** for the population mean.  
   (Use the **t-distribution** here because n is small and \\(\\sigma\\) is not known. See the table on the next page)

\newpage

## Standard Normal (Z) Distribution Table Excerpt

Left-tail probability means the $P[Z \leq z]$ is given by the right column.

| Z-Score | Left-Tail Probability |
|:------:|:----------------------:|
| 1.64 | 0.9495 |
| 1.96 | 0.9750 |
| 2.00 | 0.9772 |
| 2.05 | 0.9798 |
| 2.33 | 0.9901 |
| 2.58 | 0.9949 |



## T-Distribution Table (One-Sample, 95% CI) Using `n`

| **Sample Size** \(n\) | **t-Value** (95% CI) |
|:---------------------:|:--------------------:|
| 5                     | 2.776               |
| 6                     | 2.571               |
| 7                     | 2.447               |
| 8                     | 2.365               |
| 9                     | 2.306               |
| 10                    | 2.262               |
| 11                    | 2.228               |
| 12                    | 2.201               |
| 13                    | 2.179               |
| 14                    | 2.160               |
| 15                    | 2.145               |
| 16                    | 2.131               |
| 17                    | 2.120               |
| 18                    | 2.110               |
| 19                    | 2.101               |
| 20                    | 2.093               |
| 25                    | 2.064               |
| 30                    | 2.042               |

