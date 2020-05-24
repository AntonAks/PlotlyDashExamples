import os
import pandas as pd
import plotly.offline as pyo
import plotly.figure_factory as ff
import plotly.graph_objs as go


data_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data_samples/Data')
data_file = os.path.join(data_folder, 'iris.csv')
df = pd.read_csv(data_file)

print(df['class'].unique())


x1 = df[df['class'] == 'Iris-setosa']['petal_length']
x2 = df[df['class'] == 'Iris-versicolor']['petal_length']
x3 = df[df['class'] == 'Iris-virginica']['petal_length']

hist_data = [x1,x2,x3]

group_labels = ['Iris-setosa','Iris-versicolor','Iris-virginica']

fig = ff.create_distplot(hist_data, group_labels)
pyo.plot(fig)
