import matplotlib.pyplot as plt
import numpy as np

# Data for the social foundation (inner circle)
social_foundation = {
    "Food": 0.455,
    "Water": 0.38,
    "Income": 0.6,
    "Education": 1.0,
    "Energy": 0.5263,
    "Network": 1.0,
    "Peace & Justice": 0.1,
    "Housing": 1.0,
    "Social equality": 0.0,
    "Political voice": 0.0,
    "Gender quality": 0.5,
}

innerLabels = list(social_foundation.keys())
innerValues = list(social_foundation.values())

# Data for the ecological ceiling (outer circle)
ecological_ceiling = {
    'CO2 Emission': 1.6, 
    'Ecological Footprint': 1.8, 
    'Land-System Change': 0.36,
    'Nitrogen': 1.31, 
    'Phosphorus': 1.53,
    'Material Footprint': 0.16,
}

outerLabels = list(ecological_ceiling.keys())
outerValues = list(ecological_ceiling.values())

# Define the threshold value
thresholdValue = 3

# Setup the plot
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
ax.set_axis_off()

# Number of slices in each layer
innerN = len(innerValues)
outerN = len(outerValues)

# Define theta for both layers
theta_inner = np.linspace(0.0, 2 * np.pi, innerN, endpoint=False)
theta_outer = np.linspace(0.0, 2 * np.pi, outerN, endpoint=False)

# Define the width of each bar
width_inner = 2 * np.pi / innerN
width_outer = 2 * np.pi / outerN

# Colors
inner_color = 'lightblue'
outer_color = 'lightgreen'
exceeding_color = 'darkred'
unfilled_color = 'darkred'

# Plot the inner ring with specified color
for value, angle in zip(innerValues, theta_inner):
    ax.bar(angle, value, width=width_inner, bottom=0.2, color=inner_color,
           edgecolor='white', linewidth=1.5)
    ax.bar(angle, 1 - value, width=width_inner, bottom=0.2 + value, color=unfilled_color,
           edgecolor='white', linewidth=1.5)

# Add a wider threshold ring using the same color as the outer ring
threshold_width = 0.3  # To make the threshold ring wider
bars_threshold = ax.bar(theta_outer, [threshold_width] * outerN, width=width_outer, bottom=thresholdValue,
                        color="white", edgecolor='white', linewidth=1.5)

# Plot the outer ring with color change beyond threshold
for value, angle in zip(outerValues, theta_outer):
    bottom = 2.0
    if value + bottom > thresholdValue:
        ax.bar(angle, value, width=width_outer, bottom=bottom, color=exceeding_color,
               edgecolor='white', linewidth=1.5)
        # Draw part of the bar beneath the threshold
        ax.bar(angle, thresholdValue - bottom, width=width_outer, bottom=bottom,
               color=outer_color, edgecolor='white', linewidth=1.5)
    else:
        ax.bar(angle, value, width=width_outer, bottom=bottom, color=outer_color,
               edgecolor='white', linewidth=1.5)

# Adding labels with consistent radial position for inner circle
for bar, label in zip(theta_inner, innerLabels):
    rotation = (bar + width_inner / 2) * 180 / np.pi - 90
    ax.text(bar + width_inner / 2, 1.3,  # Slightly adjusted position
            label, ha='center', va='center', rotation=rotation + 180,
            fontsize=8, rotation_mode='anchor', transform=ax.transData)

# Adjusted labels for outer circle to be placed in the red area and aligned with the cone
for bar, label, value in zip(theta_outer, outerLabels, outerValues):
    rotation = (bar + width_outer / 2) * 180 / np.pi - 90
    
    if value + 2.0 > thresholdValue:
        # Specific adjustment for labels exceeding the threshold
        ax.text(bar + width_outer / 2, bottom + value - 0.1,  # Aligning with the top of the red area
                label, ha='center', va='center', rotation=rotation + 45,  # Adjusted rotation
                fontsize=10, rotation_mode='default', transform=ax.transData)
    else:
        ax.text(bar + width_outer / 2, bottom + value + 0.2,  # Position if below the threshold
                label, ha='center', va='center', rotation=rotation + 45,  # Adjusted rotation
                fontsize=10, rotation_mode='default', transform=ax.transData)
plt.savefig('demo.png', transparent=True)
plt.show()
