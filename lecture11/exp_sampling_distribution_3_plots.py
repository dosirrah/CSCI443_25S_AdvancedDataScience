import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def animated_sampling_distribution(n=4, initial_bins=30, max_bins=120, seed=None):
    np.random.seed(seed)
    
    lambda_param = 1  # Exponential distribution parameter (rate = 1/lambda)
    population_mean = 1 / lambda_param  # Theoretical mean of Exp(1)
    
    sample_means = []  # Stores sample means over trials
    all_samples = []   # Stores all individual sample values
    total_trials = 0   # Tracks the number of trials

    x_max = 3 / lambda_param  # ✅ Fixed x-axis range: [0, 3/lambda]

    # Set up interactive mode
    plt.ion()
    fig, axes = plt.subplots(3, 1, figsize=(8, 12), gridspec_kw={'height_ratios': [1, 3, 3]})

    # ✅ Reduce margins and spacing
    plt.subplots_adjust(left=0.05, right=0.98, top=0.96, bottom=0.06, hspace=0.22)


    def on_key(event):
        nonlocal total_trials, n, sample_means, all_samples  # Access state variables

        if event.key == 'a':  # ✅ Skip 500 samples
            num_iterations = 500  
            print(f"Advancing 500 sample means (n={n})...")
            for _ in range(num_iterations):
                total_trials += 1
                sample = np.random.exponential(scale=1/lambda_param, size=n)
                sample_mean = np.mean(sample)
                sample_means.append(sample_mean)
                all_samples.extend(sample)  # Keep accumulating samples

        elif event.key == 'n':  # ✅ Increase n and regenerate from scratch
            n += 1  
            print(f"Increasing sample size to n={n} and regenerating from scratch...")
            recompute_sample_means()

        elif event.key == 'q':  # Quit
            print("Exiting...")
            plt.close()
            return

        else:  # Default: advance by 1 sample mean
            total_trials += 1
            sample = np.random.exponential(scale=1/lambda_param, size=n)
            sample_mean = np.mean(sample)
            sample_means.append(sample_mean)
            all_samples.extend(sample)  # Keep accumulating samples

        update_plot(sample, sample_means, all_samples, total_trials)

    def recompute_sample_means():
        """ Resets and recomputes sample means with the updated `n`. """
        nonlocal total_trials
        total_trials = len(sample_means)  # Maintain number of sample means
        sample_means.clear()  # Reset sample means
        all_samples.clear()  # Reset individual sample values

        for _ in range(total_trials):  # Regenerate the same number of trials
            sample = np.random.exponential(scale=1/lambda_param, size=n)
            sample_means.append(np.mean(sample))
            all_samples.extend(sample)

        update_plot([], sample_means, all_samples, total_trials)

    def update_plot(sample, sample_means, all_samples, total_trials):
        axes[0].clear()
        axes[1].clear()
        axes[2].clear()

        # ✅ Compute Fixed Bin Width with a Cap on Max Bins
        bin_count = min(max_bins, int(30 + np.sqrt(len(sample_means) / 10)))  # ✅ Ensure bins never exceed 120
        bin_width = x_max / bin_count  # ✅ Bin width is fixed based on x-axis
        bins = np.arange(0, x_max + bin_width, bin_width)  # ✅ Ensures bins are evenly spaced

        # --- Top Plot: Current Sample ---
        if len(sample) > 0:
            y_position = 0.5
            axes[0].scatter(sample, [y_position] * len(sample), color='black', zorder=5, label="Samples")
            for x in sample:
                axes[0].text(x, y_position + 0.1, f"{x:.2f}", ha='center', fontsize=9, color='blue')

            sample_mean = np.mean(sample)
            axes[0].axvline(sample_mean, color='magenta', linestyle='-', linewidth=2, zorder=4, label="Sample Mean")

        axes[0].axvline(population_mean, color='green', linestyle='--', linewidth=2, zorder=3, label="Population Mean")
        axes[0].set_xlim(0, x_max)
        axes[0].set_ylim(0, 1)
        axes[0].set_yticks([])
        axes[0].set_title(f"Current Sample (n={n})")
        axes[0].legend(loc="upper right")

        # --- Middle Plot: Histogram of Population Samples ---
        if len(all_samples) > 0:
            axes[1].hist(all_samples, bins=bins, density=True, alpha=0.6, color='lightblue', edgecolor='black')

            x_vals = np.linspace(0, x_max, 1000)
            exp_pdf = lambda_param * np.exp(-lambda_param * x_vals)
            axes[1].plot(x_vals, exp_pdf, color='blue', linestyle='-', label="Exponential PDF")
            axes[1].axvline(population_mean, color='green', linestyle='--', linewidth=2, zorder=3, label="Population Mean")

        axes[1].set_xlim(0, x_max)
        axes[1].set_ylabel("Relative Frequency")
        axes[1].set_title("Histogram of All Sampled Values")
        axes[1].legend(loc="upper right")

        # --- Bottom Plot: Histogram of Sample Means ---
        if len(sample_means) > 0:
            axes[2].hist(sample_means, bins=bins, density=True, alpha=0.6, color='steelblue', edgecolor='black')

            x_vals = np.linspace(0, x_max, 1000)
            normal_approx = stats.norm.pdf(x_vals, loc=population_mean, scale=population_mean / np.sqrt(n))
            axes[2].plot(x_vals, normal_approx, color='red', linestyle='dashed', label="Normal Approximation")

            latest_sample_mean = sample_means[-1]
            axes[2].axvline(latest_sample_mean, color='magenta', linestyle='-', linewidth=2, zorder=4, label="Latest Sample Mean")  # ✅ Restored magenta sample mean line
            axes[2].axvline(population_mean, color='green', linestyle='--', linewidth=2, zorder=3, label="Population Mean")

        axes[2].set_xlim(0, x_max)
        axes[2].set_xlabel("Values")
        axes[2].set_ylabel("Relative Frequency")
        axes[2].set_title(f"Sampling Distribution of Sample Means (n={n}), Trials = {total_trials}")
        axes[2].legend(loc="upper right")

        plt.draw()
        plt.pause(0.01)  
        print(f"Trial {total_trials}: Sample Mean = {sample_means[-1]:.4f}")
        print("Press any key for 1 sample mean, 'a' for 500, 'n' to increase n, or 'q' to quit.")

    # Connect key press events to the function
    fig.canvas.mpl_connect('key_press_event', on_key)

    # ✅ Run the first trial automatically
    first_sample = np.random.exponential(scale=1/lambda_param, size=n)
    first_sample_mean = np.mean(first_sample)
    sample_means.append(first_sample_mean)
    all_samples.extend(first_sample)
    total_trials += 1
    update_plot(first_sample, sample_means, all_samples, total_trials)

    plt.show(block=True)  

# Run the interactive animation
animated_sampling_distribution(n=4, seed=42)
