import os
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools


data_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data_samples/Data')
df1 = pd.read_csv(os.path.join(data_folder, '2010SantaBarbaraCA.csv'))
df2 = pd.read_csv(os.path.join(data_folder, '2010YumaAZ.csv'))
df3 = pd.read_csv(os.path.join(data_folder, '2010SitkaAK.csv'))


trace1 = go.Heatmap(x=df1['DAY'], 
                    y=df1['LST_TIME'], 
                    z=df1['T_HR_AVG'].values.tolist(),
                    colorscale='Jet',
                    zmin=5,
                    zmax=40)

trace2 = go.Heatmap(x=df2['DAY'], 
                    y=df2['LST_TIME'], 
                    z=df2['T_HR_AVG'].values.tolist(),
                    colorscale='Jet',
                    zmin=5,
                    zmax=40)

trace3 = go.Heatmap(x=df3['DAY'], 
                    y=df3['LST_TIME'], 
                    z=df3['T_HR_AVG'].values.tolist(),
                    colorscale='Jet',
                    zmin=5,
                    zmax=40)

layout = go.Layout(title='Santa-Barbara temp plot')

fig = tools.make_subplots(rows=1, 
                            cols=3, 
                            subplot_titles=['2010SantaBarbaraCA','2010YumaAZ','2010SitkaAK'],
                            shared_xaxes=True)

fig.append_trace(trace1,1,1)
fig.append_trace(trace2,1,2)
fig.append_trace(trace3,1,3)

pyo.plot(fig)
