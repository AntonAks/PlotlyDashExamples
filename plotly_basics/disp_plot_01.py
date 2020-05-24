import os

import numpy as np
import plotly.offline as pyo
import plotly.figure_factory as ff
import plotly.graph_objs as go


x1 = np.random.randn(1000)-2
x2 = np.random.randn(1000)
x3 = np.random.randn(1000)+2
x4 = np.random.randn(1000)+4

hist_data = [x1,x2,x3,x4]

group_labels = ['x1','x2','x3','x4']

fig = ff.create_distplot(hist_data, group_labels, bin_size=[.2,.1,.4,1])
pyo.plot(fig)
