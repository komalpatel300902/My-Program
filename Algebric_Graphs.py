"""
This program draw Algebric graph of x to the power n.
Where n is any number between 0 to infinite.
This is User define program. User is Asked the degree of the graph.
After that the graph is plotted.
"""

# importing some essintial library
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

x = np.arange(-100,100,0.1)     # X Range of X Axis.
degree = int(input("Enter your degree of graph (0 to infinity) : "))    # user input for the degree of graph.
y = x**degree   # Y Range of Y Axis
trace = go.Scatter(x = x, y = y, mode = "lines" )   # graph that will be shown
data = [trace]  # for multiple graph

# Description of layout of graph
layout = go.Layout(title = "Algebric Graph",
                    xaxis = {"title":"X Axis"},
                    yaxis = {"title":"Y Axis"})

# getting the figure object for plotting purpose.
fig  = go.Figure(data = data , layout = layout )

# plotting the graph and saving it as Algebric_Graph.html
pyo.plot(fig,filename = "Algebric_Graph.html")
