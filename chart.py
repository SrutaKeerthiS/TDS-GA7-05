# chart.py
# This script generates a Seaborn violinplot for customer support response times.
 
# Import required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
 
# --- 1. Generate Realistic Synthetic Data ---
# The data is generated to simulate different response time distributions
# across various support channels (e.g., Live Chat is fast, Email is slower).
np.random.seed(42) # For reproducibility
live_chat_data = np.random.lognormal(mean=1.5, sigma=0.5, size=500)
phone_data = np.random.lognormal(mean=2.2, sigma=0.7, size=500)
email_data = np.random.lognormal(mean=3.0, sigma=0.9, size=500)
 
data = pd.DataFrame({
    'Response_Time_Minutes': np.concatenate([live_chat_data, phone_data, email_data]),
    'Support_Channel': ['Live Chat'] * 500 + ['Phone'] * 500 + ['Email'] * 500
})
 
# --- 2. Create and Style the Violin Plot ---
# Set a professional style for the plot
sns.set_style("whitegrid")
 
# Set the context for presentation-ready text sizes
sns.set_context("talk")
 
# Create a figure with the exact dimensions for the output
plt.figure(figsize=(8, 8))
 
# Create the violin plot
# The 'palette' parameter adds color, 'inner' adds a mini-boxplot
sns.violinplot(
    x='Support_Channel',
    y='Response_Time_Minutes',
    data=data,
    palette='viridis',
    inner='quartile'
)
 
# Set descriptive titles and labels
plt.title('Customer Support Response Time Distribution by Channel')
plt.xlabel('Support Channel')
plt.ylabel('Response Time (minutes)')
 
# --- 3. Save the Chart with Exact Dimensions ---
# Save the figure as 'chart.png' with a DPI that results in a 512x512 image (8 inches * 64 dpi)
# 'bbox_inches="tight"' ensures no extra whitespace around the plot
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
 
# Display the plot
plt.show()
 
print("Chart generated successfully and saved as 'chart.png'.")
