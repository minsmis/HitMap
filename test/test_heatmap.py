import os

import functions as fc

# Before start,
# These function needs 2D matrix color data.
# 1D array have to contain X color values.
# 2D array have to correspond to Y values.

# Variables
path = 'YOUR/DATA/FOLDER/PATH/data.mat'
storage = 'YOUR/STORAGE/FOLDER/PATH'
fname = 'test_heatmap_plot.tiff'
variables = ['value_wave_norm_mean', 'freq']

# Experiment setup
figure_size = [8, 4]
fontsize = 12
fs = 2000
x_tick_range = [-1.5, 5]  # Recorded x values
x_range = [-1, 5]  # x values to show on plot
x_tick = 1
y_range = [0, 25]
y_tick = 5
c_range = [0, 300]
colormap = 'plasma'
linewidth = 3
vlines = 0
hlines = [2.5, 4, 12]
transparency = True

# Import data
data = fc.import_data(data_path=path, import_variables=variables)

# Make x and y ticks
x_ticks = fc.make_xticks(x_range=x_tick_range, sampling_frequency=fs)
x_labels = fc.make_xlabels(x_range=x_range, tick=x_tick)
y_labels = fc.make_ylabels(y_range=y_range, tick=y_tick)

# Plot heatmap
heatmap = fc.heatmap(data=data['value_wave_norm_mean'], figure_size=figure_size,
                     x_ticks=x_ticks, y_ticks=data['freq'], x_range=x_range, y_range=y_range,
                     x_labels=x_labels, y_labels=y_labels, c_range=c_range,
                     show_colorbar=True, colormap=colormap, fontsize=fontsize,
                     linewidth=linewidth, vline=vlines, hline=hlines)

# Save plots
fc.save_figure(heatmap, os.path.join(storage, fname), transparency=transparency)
