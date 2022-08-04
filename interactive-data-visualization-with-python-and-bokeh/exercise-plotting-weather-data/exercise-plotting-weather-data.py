#library imports
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

#prepare the data
df = pandas.read_excel("verlegenhuken.xlsx")
df["Temperature"] = df["Temperature"] / 10
df["Pressure"] = df["Pressure"] / 10

#create a figure object
f = figure(plot_width=500, plot_height=400, tools='pan')

#changing plot properties
f.title.text = 'Temperature and Air Pressure'
f.title.text_color = 'gray'
f.title.text_font = 'arial'
f.title.text_font_style = 'bold'
f.xaxis.minor_tick_line_color = None
f.yaxis.minor_tick_line_color = None
f.xaxis.axis_label = 'Temperature (°C)'
f.yaxis.axis_label = 'Pressure (hPa)'

#create a line plot
f.circle(df["Temperature"], df["Pressure"], size=0.5)

#prepare the output file
output_file("temperature_and_air_pressure.html")

#write the plot in the figure object
show(f)
