import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def plot_interactive_uniform_ci(num_samples, seed=None):
    np.random.seed(seed)
    
    a, b = 0, 1  # Parameters for U[0, 1]
    mu = (a + b) / 2  # True mean
    sigma = (b - a) / np.sqrt(12)  # Population standard deviation

    # Initialize tracking counters
    total_trials = 0
    count_mu_in_ci = 0

    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots(figsize=(10, 6))

    while True:
        ax.clear()  # Clear the previous plot
        total_trials += 1  # Increment keypress count

        # Generate samples from U[0, 1]
        samples = np.random.uniform(a, b, num_samples)
        sample_mean = np.mean(samples)
        std_dev = np.std(samples, ddof=1)  # Sample standard deviation
        std_error = std_dev / np.sqrt(num_samples)  # Standard error of the mean

        # Define confidence interval using normal approximation
        ci_left, ci_right = sample_mean - 1.96 * std_error, sample_mean + 1.96 * std_error

        # Check if the true mean falls within the confidence interval
        if ci_left <= mu <= ci_right:
            count_mu_in_ci += 1

        # Compute percentage of cases where μ is in the confidence interval
        percentage_inside_ci = (count_mu_in_ci / total_trials) * 100

        # Uniform PDF shaded in gray
        x = np.linspace(a, b, 1000)
        y = stats.uniform.pdf(x, loc=a, scale=b-a)
        ax.fill_between(x, y, color='gray', alpha=0.5, label='Uniform PDF U[0, 1]')

        # True mean line
        ax.axvline(mu, color='green', linestyle='--', label='True Mean ($\mu = 0.5$)')

        # Sample points
        sample_line_y = np.max(y) + 0.2  # Slightly above the PDF
        ax.scatter(samples, [sample_line_y] * num_samples, color='black', zorder=5)

        # Sample mean line
        ax.axvline(sample_mean, color='magenta', linestyle='-', label='Sample Mean ($\overline{x}$)')

        # Confidence interval (CI) arrows
        ax.annotate('', xy=(ci_left, sample_line_y + 0.15), xytext=(ci_right, sample_line_y + 0.15),
                    arrowprops=dict(arrowstyle="<->", lw=1.5, color='red'))

        # CI annotation
        ci_annotation = r"$95\% \, \text{CI} = \overline{x} \pm 1.96 \cdot \text{SE}$"
        ax.text(sample_mean, sample_line_y + 0.25, ci_annotation, horizontalalignment='center', color='red',
                bbox=dict(facecolor='white', alpha=1, edgecolor='none'))

        # Display percentage of times μ is inside CI (Lower-right corner)
        stats_text = f"Trials: {total_trials}\nμ inside CI: {count_mu_in_ci} ({percentage_inside_ci:.2f}%)"
        ax.text(0.98, 0.02, stats_text, fontsize=12, color='blue', transform=ax.transAxes,
                horizontalalignment='right', verticalalignment='bottom',
                bbox=dict(facecolor='white', alpha=1, edgecolor='black'))

        # Adjust y-limits for visualization
        ax.set_ylim(bottom=0, top=1.8)

        # Labels and title
        ax.set_xlabel('X value')
        ax.set_ylabel('Probability Density')
        ax.set_title(f'Interactive Confidence Interval Visualization (n={num_samples})')
        ax.legend(loc='upper right')

        # Adjust x-limits
        ax.set_xlim(min(ci_left, a - 0.05), max(ci_right, b + 0.05))

        plt.draw()  # Draw the plot
        print(f"Sample {total_trials}: Mean = {sample_mean:.4f}, CI = [{ci_left:.4f}, {ci_right:.4f}], μ Inside CI: {ci_left <= mu <= ci_right}")
        print(f"Total Trials: {total_trials}, Count μ in CI: {count_mu_in_ci}, Percentage: {percentage_inside_ci:.2f}%")

        # Wait for keypress to generate new sample
        print("Press any key for a new sample (or close the plot window to exit)...")
        if not plt.waitforbuttonpress():  # Block until keypress
            break

    plt.ioff()  # Turn off interactive mode
    plt.close()

# Run the interactive plot
plot_interactive_uniform_ci(num_samples=10, seed=51)

