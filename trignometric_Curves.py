# This program plot Sine and Cosine curve

'''
This program use files from plotly and numpy module.
Before running this program please ensure that this modules are in your PC.
'''

# Initialising modules
import plotly.offline as pyo   
import plotly.graph_objs as go 
import numpy as np 

# This is array of number which will be used for ploat the graph
x = np.arange(0,50,0.1) # Points of X Axis of graph
y1 = 1*np.sin(x)        # Points of Y Axis  of sine graph 
y2 = 1*np.cos(x)        # Points of Y Axis of Cosine graph

trace1 = go.Scatter(x = x, y = y1 , mode = "lines", marker = {"color": "#151519"}, name = "Sine" ) # This is graph of sine
trace2 = go.Scatter(x = x, y = y2 , mode = "lines" ,name = "Cosine")                               # This is graph of cosine
data = [trace1, trace2] # Taking graph in a list 

layout = go.Layout(title = "Trinometric Curves",
                  xaxis = {"title": "X-Axis"},
                  yaxis = {"title": "Y-Axis"}) # This describe the graph

fig = go.Figure(data = data, layout = layout)       # Figure object is created for ploting 
pyo.plot(fig, filename = "Sine_Cosine_Curve.html")  # Graph is ploted and saved in Sine_Cosine_Curve.html 