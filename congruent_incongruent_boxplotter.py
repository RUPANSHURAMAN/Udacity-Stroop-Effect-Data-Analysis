# import necessary lib
import matplotlib.pyplot as plot 

# create congruent and incongruent data
congruent_data = [12.079, 16.791, 9.564, 8.63, 14.669, 12.238, 14.692, 8.987, 9.401, 14.48, 22.328, 15.298, 15.073, 16.929, 18.2, 12.13, 18.495, 10.639, 11.344, 12.369, 12.944, 14.233, 19.71, 16.004]
incongruent_data = [19.278, 18.741, 21.214, 15.687, 22.803, 20.878, 24.572, 17.394, 20.762, 26.282, 24.524, 18.644, 17.51, 20.33, 35.255, 22.158, 25.139, 20.429, 17.425, 34.288, 23.894, 17.96, 22.058, 21.157]

# add both congruent and incongruent data in a single list
data_to_plot = [congruent_data, incongruent_data]

# Create a figure instance
fig = plot.figure(1, figsize=(10, 7))

# Create an axes instance
axes = fig.add_subplot(111)

# Create the boxplot
bplot = axes.boxplot(data_to_plot)

## set axes.boxplot() to True to fill color 
bplot = axes.boxplot(data_to_plot, patch_artist=True)

## change outline and fill color of boxes
for box in bplot['boxes']:
    # change outline color
    box.set(color='#FF1744', linewidth=2)
    # change face color
    box.set(facecolor = '#2196F3')

# set x-axis labels to 'Congruent' and 'Incongruent'
axes.set_xticklabels(['Congruent', 'Incongruent'])

# Save the figure
fig.savefig('boxplot.png', bbox_inches='tight')