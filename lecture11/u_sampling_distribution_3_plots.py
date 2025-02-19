import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def animated_sampling_distribution(n=4, initial_bins=30, max_bins=120, seed=None):
    np.random.seed(seed)
    
    a, b = 0, 1  # Uniform U[0,1] parameters
    population_mean = (a + b) / 2  # Mean of U[0,1] is 0.5
    population_std_dev = (b - a) / np.sqrt(12)  # Standard deviation of U[0,1]

    sample_means = []  # Stores sample means over trials
    all_samples = []   # Stores all individual sample values
    total_trials = 0   # Tracks the number of trials

    buffer = 0.2  # ✅ Extra padding for X-axis
    x_min, x_max = a - buffer, b + buffer  # ✅ Extend X-axis range

    # Set up interactive mode
    plt.ion()
    fig, axes = plt.subplots(3, 1, figsize=(8, 12), gridspec_kw={'height_ratios': [0.5, 2, 2]})  # ✅ Reduce top plot height
    plt.subplots_adjust(left=0.08, right=0.98, top=0.95, bottom=0.08, hspace=0.3)  # ✅ Reduce margins

    def on_key(event):
        nonlocal total_trials, n, sample_means, all_samples  

        sample = []  # ✅ Ensure `sample` is always initialized

        if event.key == 'a':  # ✅ Advance 500 sample means
            num_iterations = 500  
            print(f"Advancing 500 sample means (n={n})...")
            for _ in range(num_iterations):
                total_trials += 1
                sample = np.random.uniform(a, b, size=n)
                sample_mean = np.mean(sample)
                sample_means.append(sample_mean)
                all_samples.extend(sample)

        elif event.key == 'n':  # ✅ Increase n and regenerate from scratch
            n += 1  
            print(f"Increasing sample size to n={n} and regenerating from scratch...")
            recompute_sample_means()
            return

        elif event.key == 'q':  # Quit
            print("Exiting...")
            plt.close()
            return

        else:  # Default: advance by 1 sample mean
            total_trials += 1
            sample = np.random.uniform(a, b, size=n)
            sample_mean = np.mean(sample)
            sample_means.append(sample_mean)
            all_samples.extend(sample)

        update_plot(sample, sample_means, all_samples, total_trials)

    def recompute_sample_means():
        """ Resets and recomputes sample means with the updated `n`. """
        nonlocal total_trials
        total_trials = len(sample_means)  # Maintain number of sample means
        sample_means.clear()
        all_samples.clear()

        for _ in range(total_trials):  # Regenerate the same number of trials
            sample = np.random.uniform(a, b, size=n)
            sample_means.append(np.mean(sample))
            all_samples.extend(sample)

        update_plot([], sample_means, all_samples, total_trials)

    def update_plot(sample, sample_means, all_samples, total_trials):
        axes[0].clear()
        axes[1].clear()
        axes[2].clear()

        # ✅ Compute Fixed Bin Width with a Cap on Max Bins
        bin_count = min(max_bins, int(30 + np.sqrt(len(sample_means) / 10)))  # ✅ Cap at 120 bins
        bin_width = (x_max - x_min) / bin_count
        bins = np.arange(x_min, x_max + bin_width, bin_width)  # ✅ Ensures bins are evenly spaced

        # --- Top Plot: Current Sample ---
        y_position = 0.5
        axes[0].scatter(sample, np.full_like(sample, y_position), color='black', zorder=5, label="Samples")

        for x in sample:
            axes[0].text(x, y_position - 0.1, f"{x:.2f}", ha='center', fontsize=9, color='blue')  # ✅ Lower labels

        sample_mean = np.mean(sample)
        axes[0].axvline(sample_mean, color='magenta', linestyle='-', linewidth=2, label="Sample Mean")  # ✅ Magenta Line for Sample Mean
        axes[0].axvline(population_mean, color='green', linestyle='dotted', linewidth=2, label="Population Mean (True)")
        
        axes[0].set_xlim(x_min, x_max)
        axes[0].set_yticks([])
        axes[0].set_title(f"Current Sample (n={n})")
        axes[0].legend(loc="upper right")

        # --- Middle Plot: Histogram of All Samples ---
        axes[1].hist(all_samples, bins=bins, density=True, alpha=0.6, color='lightblue')
        axes[1].fill_between([a, b], 0, 1, color='gray', alpha=0.5, label="Uniform U[0,1] PDF")  # ✅ Increased alpha to 0.5
        axes[1].set_xlim(x_min, x_max)
        axes[1].set_ylabel("Relative Frequency")
        axes[1].set_title(f"Distribution of Individual Samples (n={n})")
        axes[1].legend(loc="upper right")

        # --- Bottom Plot: Histogram of Sample Means ---
        if len(sample_means) > 0:
            axes[2].hist(sample_means, bins=bins, density=True, alpha=0.6, color='lightblue')

            # ✅ Gaussian Approximation
            x_vals = np.linspace(x_min, x_max, 1000)
            normal_approx = stats.norm.pdf(x_vals, loc=population_mean, scale=population_std_dev / np.sqrt(n))
            axes[2].plot(x_vals, normal_approx, color='green', linestyle='-', label="Gaussian Approximation")

            # ✅ Standard Error Indicator
            std_error = population_std_dev / np.sqrt(n)
            se_left, se_right = population_mean - std_error, population_mean + std_error
            y_midpoint = 0.5 * max(axes[2].get_ylim())  # Place line in middle of histogram
            axes[2].annotate('', xy=(se_left, y_midpoint), xytext=(se_right, y_midpoint),
                             arrowprops=dict(arrowstyle="<->", color='magenta', lw=2))
            axes[2].text(population_mean, y_midpoint + 0.05, "Std Error", ha='center', color='magenta', fontsize=12)

            # ✅ Vertical Lines
            latest_sample_mean = sample_means[-1]
            axes[2].axvline(latest_sample_mean, color='magenta', linestyle='-', linewidth=2, zorder=4, label="Latest Sample Mean")
            axes[2].axvline(population_mean, color='green', linestyle='dotted', linewidth=2, label="Population Mean (True)")

        axes[2].set_xlim(x_min, x_max)
        axes[2].set_xlabel("Values")
        axes[2].set_ylabel("Relative Frequency")
        axes[2].set_title(f"Sampling Distribution of Sample Means (n={n}), Trials = {total_trials}")
        axes[2].legend(loc="upper right")

        plt.draw()
        plt.pause(0.01)
        print(f"Trial {total_trials}: Sample Mean = {sample_means[-1]:.4f}")

    # Connect key press events to the function
    fig.canvas.mpl_connect('key_press_event', on_key)

    # ✅ Run the first trial automatically
    first_sample = np.random.uniform(a, b, size=n)
    sample_means.append(np.mean(first_sample))
    all_samples.extend(first_sample)
    total_trials += 1
    update_plot(first_sample, sample_means, all_samples, total_trials)

    plt.show(block=True)  

# Run the interactive animation
animated_sampling_distribution(n=4, seed=42)

