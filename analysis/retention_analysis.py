
import matplotlib.pyplot as plt
import numpy as np
import os

# --- Data ---
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
retention_rates = [68.35, 69.02, 75.00, 77.94]
industry_benchmark = 85.00
average_retention = np.mean(retention_rates)

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot quarterly retention rates
ax.plot(quarters, retention_rates, marker='o', linestyle='-', color='dodgerblue', label='Quarterly Retention Rate')
ax.scatter(quarters, retention_rates, color='dodgerblue', s=100)

# Add value labels to each point
for i, txt in enumerate(retention_rates):
    ax.annotate(f'{txt:.2f}', (quarters[i], retention_rates[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10)

# Plot average retention rate
ax.axhline(y=average_retention, color='gray', linestyle='--', linewidth=1.5, label=f'Average Retention ({average_retention:.2f})')

# Plot industry benchmark
ax.axhline(y=industry_benchmark, color='red', linestyle='--', linewidth=1.5, label=f'Industry Benchmark ({industry_benchmark:.2f})')

# --- Aesthetics and labels ---
ax.set_title('2024 Quarterly Customer Retention vs. Industry Benchmark', fontsize=16, pad=20)
ax.set_xlabel('Quarter', fontsize=12)
ax.set_ylabel('Retention Rate (%)', fontsize=12)
ax.set_ylim(65, 90)
ax.legend(frameon=True, shadow=True)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# --- Save the figure ---
output_dir = 'analysis/figures'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'retention_trend_vs_benchmark.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')

print(f"Chart saved to {output_path}")
print(f"Average retention rate: {average_retention:.2f}")
