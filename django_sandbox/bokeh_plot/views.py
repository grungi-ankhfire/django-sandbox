from django.views.generic.base import TemplateView
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import math
import numpy as np

# Create your views here.


class BokehView(TemplateView):
    template_name = "bokeh_plot/bokeh.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BokehView, self).get_context_data(**kwargs)

        x = np.arange(0.0, 7.0, 0.1)
        y = [math.cos(a) for a in x]

        title = 'y = cos(x)'

        plot = figure(
            title=title,
            x_axis_label='X-Axis',
            y_axis_label='Y-Axis',
            plot_width=400,
            plot_height=400)

        plot.line(x, y, legend='f(x)', line_width=2)
        # Store components
        script, div = components(plot)

        context['script'] = script
        context['div'] = div
        return context
