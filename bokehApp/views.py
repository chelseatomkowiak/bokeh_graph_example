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
    waterInList = []
    #THIS WORKS    waterOutList = [4, 5, 6]
    waterOutList = []
    for CurrentStats.waterIn in tempp:
        waterInList += [7, 8, 9]
#    for CurrentStats.waterOut in tempp:
#        waterOutList += [CurrentStats.waterOut]
    for e in tempp:
        waterOutList += e.waterOut
    numInWaterInList = len(waterInList)
    numInWaterOutList = len(waterOutList)
    numMinusOneWaterIn = (numInWaterInList - 1)
    numMinusOneWaterOut = (numInWaterOutList - 1)
    currentWaterIn = waterInList[numMinusOneWaterIn]
    currentWaterOut = waterOutList[numMinusOneWaterOut]
    counts = []
    counts.extend([currentWaterIn, currentWaterOut])
    plot = figure(x_range=items, plot_height=600, plot_width=600, title="Temperature", toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset,tap")
    plot.title.text_font_size = '20pt'
    plot.xaxis.major_label_text_font_size = '14pt'
    plot.vbar(items, top=counts, width=.4, color="navy", legend="Current Temperature")
    plot.legend.label_text_font_size = '14pt'
    script, div = components(plot)
    return render(request, 'starter.html', {'script': script, 'div': div, 'waterOutList': waterOutList, 'waterInList': waterInList, 'tempp': tempp, 'counts': counts, 'items': items, 'numInWaterInList': numInWaterInList, 'numInWaterOutList': numInWaterOutList, 'numMinusOneWaterIn': numMinusOneWaterIn, 'numMinusOneWaterOut': numMinusOneWaterOut, 'currentWaterIn': currentWaterIn, 'currentWaterOut': currentWaterOut})
