import plotly.offline as pyo
import plotly.graph_objs as go


# y = [1,5,7,8,3,2,34,7,5,68,2,1,32,12,16,18,14,46,34,2,7,5,23,44]
# data = [go.Box(y=y, boxpoints='all', jitter=0.3, pointpos=0)]
# pyo.plot(data)

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

data = [go.Box(y=snodgrass, name='Snodgrass'),
        go.Box(y=twain, name='Twain'),]

pyo.plot(data)




