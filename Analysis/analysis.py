# Imports
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# Set professional matplotlib settings
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.figsize'] = (8, 6)

# Professional color palette
colors = {
    'navy': '#2E4057',    # Original Carleton Central
    'teal': '#3E8E9E',    # Figma
    'gray': '#8D9CA8'     # Secondary elements
}

# Data with only time-related columns for Hypothesis 3
data = pd.DataFrame({
    'Participant': ['P1', 'P1', 'P2', 'P2', 'P3', 'P3', 'P4', 'P4', 'P5', 'P5', 'P6', 'P6'],
    'Interface': ['Original', 'Figma', 'Original', 'Figma', 'Original', 'Figma', 
                  'Original', 'Figma', 'Original', 'Figma', 'Original', 'Figma'],
    'Time_s': [183, 76, 200, 90, 199, 88, 220, 79, 180, 55, 250, 103]
})

# Split data
orig_times = data[data['Interface'] == 'Original']['Time_s']
figma_times = data[data['Interface'] == 'Figma']['Time_s']

# Paired t-test for time
t_stat, p_value = stats.ttest_rel(orig_times, figma_times)

# Descriptive statistics
def get_stats(data):
    return data.mean(), data.std()

time_orig_m, time_orig_sd = get_stats(orig_times)
time_figma_m, time_figma_sd = get_stats(figma_times)

# Line Graph for Hypothesis 3
plt.figure()
participants = data['Participant'].unique()
x_axis = range(len(participants))
plt.plot(x_axis, orig_times, marker='o', color=colors['navy'], linestyle='-', linewidth=2.5, label='Original Carleton Central')
plt.plot(x_axis, figma_times, marker='o', color=colors['teal'], linestyle='-', linewidth=2.5, label='Figma')
plt.xticks(x_axis, participants)
plt.title('Task Completion Time by Participant', pad=15)
plt.xlabel('Participant')
plt.ylabel('Time (seconds)')
plt.ylim(0, 300)
plt.text(0.05, 0.95, f'Paired t-test p-value < 0.01', transform=plt.gca().transAxes, fontsize=12, 
         bbox=dict(facecolor='white', edgecolor='black', alpha=0.9))
plt.legend(loc='upper right', frameon=True, edgecolor='black')
plt.grid(True, linestyle='--', alpha=0.3, color=colors['gray'])
plt.savefig('line_time_h3.pdf', bbox_inches='tight', dpi=300)
plt.show()

# Save raw data (optional, kept for consistency)
data.to_csv('raw_data_h3.csv', index=False)
