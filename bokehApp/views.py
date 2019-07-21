from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource

from bokeh.palettes import Category20c, Spectral6
from bokeh.transform import cumsum
from .models import CurrentStats
from numpy import pi
# import pandas as pd
from bokeh.resources import CDN


def products(request):
    items = ["Incoming Water", "Outgoing Water"]
    tempp = [CurrentStats.objects.all()]
    waterInList = [1, 2, 3]
    waterOutList = [4, 5, 6]
    currentWaterIn = 195
    currentWaterOut = 170
    counts = []
    counts.extend([currentWaterIn, currentWaterOut])
    plot = figure(x_range=items, plot_height=600, plot_width=600, title="Temperature", toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset,tap")
    plot.title.text_font_size = '20pt'
    plot.xaxis.major_label_text_font_size = '14pt'
#   plot.vbar(items, top=counts, width=.4, color="green", legend="Current Temperature")
    plot.vbar(items, top=counts, width=.4, color="green")
    plot.legend.label_text_font_size = '14pt'
    script, div = components(plot)
    return render(request, 'starter.html', {'script': script, 'div': div, 'waterOutList': waterOutList, 'waterInList': waterInList, 'tempp': tempp, 'counts': counts, 'items': items, 'currentWaterIn': currentWaterIn, 'currentWaterOut': currentWaterOut})
