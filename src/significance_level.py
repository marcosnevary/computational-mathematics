import numpy as np
from scipy.stats import ttest_ind

num_simulations = 10000
sample_size = 30
true_mean = 50
true_std = 10
significance_level = 0.05 # Usar valores diferentes
significant_results = 0

for _ in range(num_simulations):
    group1 = np.random.normal(true_mean, true_std, sample_size)
    group2 = np.random.normal(true_mean, true_std, sample_size)

    t_stat, p_value = ttest_ind(group1, group2)

    if p_value < significance_level:
        significant_results += 1

proportion_significant = significant_results / num_simulations
print(f'Number of simulations: {num_simulations}')
print(f'Significance level (alpha): {significance_level}')
print(f'Proportion of significant results (Type I error rate): {proportion_significant:.4f}')
