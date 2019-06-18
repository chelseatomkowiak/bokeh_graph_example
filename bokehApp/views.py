from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from bokeh.plotting import figure, output_file
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource
from bokeh.palettes import Category20c, Spectral6
from bokeh.transform import cumsum
from numpy import pi
# import pandas as pd
from bokeh.resources import CDN

def programming(request):
    lang = ['Imcoming Water', 'Outgoing Water']
    counts = [190, 175]

    p = figure(x_range=lang, plot_height=450, title="Temperature",
               toolbar_location="below", tools="pan,wheel_zoom,box_zoom,reset, tap")

    source = ColumnDataSource(data=dict(lang=lang, counts=counts, color=Spectral6))
    p.add_tools(LassoSelectTool())
    p.add_tools(WheelZoomTool())

    p.vbar(x='lang', top='counts', width=.8, color='color', legend="lang", source=source)
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    p.xgrid.grid_line_color = "black"
    p.y_range.start = 0
    p.line(x=lang, y=counts, color="black", line_width=2)

    script, div = components(p)

    return render(request, 'starter.html', {'script': script, 'div': div})
