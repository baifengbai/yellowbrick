# yellowbrick.missing.bar
# Missing Values Bar Visualizer
#
# Author:  Nathan Danielsen <nathan.danielsen@gmail.com>
# Created: Fri Mar 29 5:17:36 2018 -0500
#
# Copyright (C) 2018 District Data Labs
# For license information, see LICENSE.txt
#
# ID: bar.py [] nathan.danielsen@gmail.com.com $

"""
Implementation of missing values visualizers

To Include:
- Bar
- Density Matrix (by time, specifiable index)
- Heatmap

"""

##########################################################################
## Imports
##########################################################################

import numpy as np
import matplotlib.pyplot as plt

from .base import MissingDataVisualizer

# from yellowbrick.style.colors import resolve_colors



##########################################################################
## MissingValuesBar Visualizer
##########################################################################


class MissingValuesBar(MissingDataVisualizer):
    """
    """

    def __init__(self, width=0.5, color='black', **kwargs):
        """
        """

        super(MissingValuesBar, self).__init__(**kwargs)
        self.width = width  # the width of the bars
        self.color = color  # the color of the bars

    def get_nan_col_counts(self, **kwargs):
        nan_matrix = self.X.astype(np.float)

        nan_col_counts =  [np.count_nonzero(np.isnan(col)) for col in nan_matrix.T]
        print(nan_col_counts)
        return nan_col_counts

    def draw(self, X, y, **kwargs):
        """Called from the fit method, this method generated a bar plot.
        """
        nan_col_counts = self.get_nan_col_counts()

        self.ind = np.arange(len(self.features_))  # the x locations for the groups

        self.ax.barh(self.ind - self.width / 2, nan_col_counts, self.width,
                        color=self.color)

    def finalize(self, **kwargs):
        """
        Finalize executes any subclass-specific axes finalization steps.
        The user calls poof and poof calls finalize.

        Parameters
        ----------
        kwargs: generic keyword arguments.

        """
        # Set the title
        self.set_title(
            'Missing Values by Column'
        )
        tick_locations = np.arange(len(self.features_))  # the x locations for the groups
        # Remove the ticks from the graph
        self.ax.set_ylabel('Count')
        self.ax.set_xticks(tick_locations)
        self.ax.set_xticklabels(self.features_, rotation='vertical')
        # Add the legend
        self.ax.legend(loc='best')
