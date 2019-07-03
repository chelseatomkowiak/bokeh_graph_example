from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource

from bokeh.palettes import Category20c, Spectral6
from bokeh.transform import cumsum
from .models import Products
from .models import CurrentStats
from numpy import pi
# import pandas as pd
from bokeh.resources import CDN


def products(request):
    items = ["Incoming Water", "Outgoing Water"]
    waterInn = CurrentStats.objects.values()[:1]
#    test = CurrentStats.objects.filter('updated_at').values('waterOut')
    waterIn = 0
    waterOut = 175
    counts = []

    for i in waterInn:
        if "waterIn" in i.values():
            waterIn += CurrentStats.waterIn
        if "waterOut" in i.values():
            waterOut += CurrentStats.waterOut
    counts.extend([waterIn, waterOut])

    plot = figure(x_range=items, plot_height=600, plot_width=600, title="Temperature", toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset,tap")
    plot.title.text_font_size = '20pt'
    plot.xaxis.major_label_text_font_size = '14pt'
    plot.vbar(items, top=counts, width=.4, color="navy", legend="Current Temperature")
    plot.legend.label_text_font_size = '14pt'
    script, div = components(plot)
    return render(request, 'starter.html', {'script': script, 'div': div, 'waterInn': waterInn, 'counts': counts, 'items': items, 'waterIn': waterIn, 'waterOut': waterOut})
