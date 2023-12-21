import numpy as np

import matplotlib.pyplot as plt


def make_xticks(x_range, sampling_frequency):
    # Parameters
    # 'x_range' [ndarr or list, 2 element [min, max], second]: Minimum X and maximum x.
    # 'sampling_frequency' [int]: Sampling frequency of data to make plot.

    # Check parameters
    if not isinstance(x_range, np.ndarray) and not isinstance(x_range, list):
        # Report parameter type error.
        print("Check parameter types of 'x_range'.")
        return 0
    if len(x_range) > 2:
        # Report parameter length error.
        print("Check parameter length of 'x_range'.")
        return 0
    if not isinstance(sampling_frequency, int):
        # Report parameter type error.
        print("Check parameter types of 'sampling_frequency'.")
        return 0

    # Variables
    x_start, x_stop = x_range
    x_step = 1 / sampling_frequency

    # Make original x values sampled by sampling frequency.
    x_ticks = np.arange(start=x_start, stop=x_stop, step=x_step)

    return x_ticks


def make_xlabels(x_range, tick):
    # Parameters
    # 'x_range' [ndarr or list, 2 element [min, max], second]: Minimum X and maximum x.
    # 'tick' [int, second]: X tick interval.

    # Check parameters
    if not isinstance(x_range, np.ndarray) and not isinstance(x_range, list):
        # Report parameter type error.
        print("Check parameter types of 'x_range'.")
        return 0
    if len(x_range) > 2:
        # Report parameter length error.
        print("Check parameter length of 'x_range'.")
        return 0
    if not isinstance(tick, int) and not isinstance(tick, float):
        # Report parameter type error.
        print("Check parameter types of 'tick'.")
        return 0

    # Variables
    x_start, x_stop = x_range

    # Make x ticks and labels to show.
    x_labels = np.arange(start=x_start, stop=x_stop + tick, step=tick)

    return x_labels


def make_ylabels(y_range, tick):
    # Parameters
    # 'y_range' [ndarr or list, 2 element [min, max], second]: Minimum Y and maximum y.
    # 'tick' [ndarr or list, second]: Y tick interval.

    # Check parameters
    if not isinstance(y_range, np.ndarray) and not isinstance(y_range, list):
        # Report parameter type error.
        print("Check parameter types of 'x_range'.")
        return 0
    if len(y_range) > 2:
        # Report parameter length error.
        print("Check parameter length of 'x_range'.")
        return 0
    if not isinstance(tick, int) and not isinstance(tick, float):
        # Report parameter type error.
        print("Check parameter types of 'tick'.")
        return 0

    # Variables
    y_start, y_stop = y_range

    # Make y labels to show
    y_labels = np.arange(start=y_start, stop=y_stop + tick, step=tick)

    return y_labels


def heatmap(data, **kwargs):
    # This function is for making heatmap plot using matplotlib.
    #
    # Parameters
    # 'data' [2D ndarr]: Data to draw heatmap.
    #
    # kwargs
    # 'figure_size' [ndarr or list, 2 elements [width, height]]: Figure size.
    # 'font' [str, Default='sans-serif']: Set font family.
    # 'fontsize' [int, Default=12]: Set font size.
    # 'x_ticks' [1D ndarr]: Set value for X axis.
    # 'y_ticks' [1D ndarr]: Set value for Y axis.
    # 'x_range' [ndarr or list, 2 elements [min, max]]: Set X axis range.
    # 'y_range' [ndarr or list, 2 elements [min, max]]: Set Y axis range.
    # 'x_labels' [ndarr or list]: Set X labels.
    # 'y_labels' [ndarr or list]: Set Y labels.
    # 'c_range' [ndarr or list, 2 elements [min, max], %]: Set color range.
    # 'show_colorbar' [bool, Default=True]: Show or not show color bar.
    # 'colormap' [str, Default='viridis']: Set colormaps for heatmap. Refer matplotlib colormap.
    #  For colormap, you can use representatively these colormaps, ['plasma', 'inferno', 'magma', 'binary', ...].
    # 'linewitdh' [int or float, Default=3]: Set line width.
    # 'vline' [int or float, X tick; ndarr or list, X ticks]: Add vertical line(s) on the plot.
    # 'hline' [int or fload, Y tick; ndarr or list, Y ticks ]: Add horizontal line(s) on the plot.

    # Variables
    x_ticks = []
    y_ticks = []

    # matplotlib default parameters
    FONTFAMILY = 'sans-serif'
    FONTSIZE = 12
    LINEWIDTH = 3

    # Make figure
    figure = plt.figure()
    if 'figure_size' in kwargs:
        figure_size = kwargs.get('figure_size')
        if isinstance(figure_size, np.ndarray) or isinstance(figure_size, list):
            width, height = figure_size
            figure = plt.figure(figsize=(width, height))
        if not isinstance(figure_size, np.ndarray) and not isinstance(figure_size, list):
            print("Check the type of 'figure_size'.")

    # Set font family
    if 'font' in kwargs:
        temp_font = kwargs.get('font')
        if isinstance(temp_font, str):
            FONTFAMILY = temp_font
    plt.rc('font', family=FONTFAMILY)  # controls default font family

    # Set font size
    if 'fontsize' in kwargs:
        temp_fontsize = kwargs.get('fontsize')
        if isinstance(temp_fontsize, int):
            FONTSIZE = temp_fontsize
    plt.rc('font', size=FONTSIZE)  # controls default text sizes

    # Get X axis data from kwargs
    if 'x_ticks' in kwargs:
        temp_x_ticks = kwargs.get('x_ticks')
        if isinstance(temp_x_ticks, list) or isinstance(temp_x_ticks, np.ndarray):
            if np.ndim(temp_x_ticks) == 1:
                x_ticks = np.array(temp_x_ticks)
            if np.ndim(temp_x_ticks) > 1:
                print("Check the dimension of 'x_ticks'.")
        if not isinstance(temp_x_ticks, list) and not isinstance(temp_x_ticks, np.ndarray):
            print("Check the type of 'x_ticks'.")

    # Get Y axis data from kwargs
    if 'y_ticks' in kwargs:
        temp_y_ticks = kwargs.get('y_ticks')
        if isinstance(temp_y_ticks, list) or isinstance(temp_y_ticks, np.ndarray):
            if np.ndim(temp_y_ticks) == 1:
                y_ticks = np.array(temp_y_ticks)
            if np.ndim(temp_y_ticks) > 1:
                print("Check the dimension of 'x_ticks'.")
        if not isinstance(temp_y_ticks, list) and not isinstance(temp_y_ticks, np.ndarray):
            print("Check the type of 'x_ticks'.")

    # Draw heatmap
    if len(x_ticks) == 0 and len(y_ticks) == 0:
        # When only color data was given.
        plt.pcolor(data)

    if len(x_ticks) == 0 and len(y_ticks) != 0:
        # When x-axis and color data were given.
        y_ticks = np.arange(0, np.size(data, 0))
        plt.pcolor(x_ticks, y_ticks, data)

    if len(x_ticks) != 0 and len(y_ticks) == 0:
        # When y-axis and color data were given.
        x_ticks = np.arange(0, np.size(data, 1))
        plt.pcolor(x_ticks, y_ticks, data)

    if len(x_ticks) != 0 and len(y_ticks) != 0:
        # When x- and y-axis and color data were given.
        plt.pcolor(x_ticks, y_ticks, data)

    # Show color bar
    if 'show_colorbar' in kwargs:
        show_colorbar = kwargs.get('show_colorbar')
        if isinstance(show_colorbar, bool):
            if show_colorbar is True:
                plt.colorbar()
    if 'show_colorbar' not in kwargs:  # Default is showing color bar.
        plt.colorbar()

    # Set x-axis range
    if 'x_range' in kwargs:
        x_range = kwargs.get('x_range')
        if isinstance(x_range, np.ndarray) or isinstance(x_range, list):
            plt.xlim(list(x_range))

    # Set y-axis range
    if 'y_range' in kwargs:
        y_range = kwargs.get('y_range')
        if isinstance(y_range, np.ndarray) or isinstance(y_range, list):
            plt.ylim(list(y_range))

    # Set x-axis ticks
    if 'x_labels' in kwargs:
        x_labels = kwargs.get('x_labels')
        if isinstance(x_labels, np.ndarray) or isinstance(x_labels, list):
            plt.xticks(x_labels)

    # Set y-axis ticks
    if 'y_labels' in kwargs:
        y_labels = kwargs.get('y_labels')
        if isinstance(y_labels, np.ndarray) or isinstance(y_labels, list):
            plt.yticks(y_labels)

    # Set color range
    if 'c_range' in kwargs:
        c_range = kwargs.get('c_range')
        if isinstance(c_range, np.ndarray) or isinstance(c_range, list):
            plt.clim(list(c_range))

    # Set colormap
    if 'colormap' in kwargs:
        colormap = kwargs.get('colormap')
        if isinstance(colormap, str):
            plt.set_cmap(colormap)

    # Set line width
    if 'linewidth' in kwargs:
        temp_linewidth = kwargs.get('linewidth')
        if isinstance(temp_linewidth, int) or isinstance(temp_linewidth, float):
            LINEWIDTH = temp_linewidth

    # Add vertical line(s)
    if 'vline' in kwargs:
        vline = kwargs.get('vline')
        # Add single vertical line
        if isinstance(vline, int) or isinstance(vline, float):
            plt.axvline(vline, color='white', linestyle='dotted', linewidth=LINEWIDTH)
        # Add multiple vertical lines
        if isinstance(vline, np.ndarray) or isinstance(vline, list):
            for v_tick in vline:
                plt.axvline(v_tick, color='white', linestyle='dotted', linewidth=LINEWIDTH)

    # Add horizontal line(s)
    if 'hline' in kwargs:
        hline = kwargs.get('hline')
        # Add single horizontal line
        if isinstance(hline, int) or isinstance(hline, float):
            plt.axhline(hline, color='white', linestyle='dotted', linewidth=LINEWIDTH)
        # Add multiple horizontal lines
        if isinstance(hline, np.ndarray) or isinstance(hline, list):
            for h_tick in hline:
                plt.axhline(h_tick, color='white', linestyle='dotted', linewidth=LINEWIDTH)

    # Show plot
    plt.show()
    return figure


def save_figure(figure, fpath, **kwargs):
    # Parameters
    # 'figure' [Figure]: Matplotlib pyplot figure object to save.
    # 'fpath' [str]: Path to save. It must contain full path and file name with extension.
    #
    # kwargs
    # 'transparency' [bool, Default=False]: Set background transparency.

    # Check parameters
    if not isinstance(figure, type(plt.figure())):
        # Report parameter type error.
        print("Check parameter types of 'figure'.")
        return 0
    if not isinstance(fpath, str):
        # Report parameter type error.
        print("Check parameter types of 'fpath'.")
        return 0

    # Export mode
    TRANSPARENCY = False
    if 'transparency' in kwargs:
        temp_transparency = kwargs.get('transparency')
        if isinstance(temp_transparency, bool):
            TRANSPARENCY = temp_transparency

    # Save figure
    figure.savefig(fpath, transparent=TRANSPARENCY)
