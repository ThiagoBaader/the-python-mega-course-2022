#library import
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

#prepare the data
df = pandas.read_csv("bachelors.csv")
x = df["Year"]
y = df["Engineering"]

#prepare the output file
output_file("Line_from_csv.html")

#create a figure object
f = figure()

#create a line plotting
f.line(x, y)

#write the plot in the figure objetc
show(f)
