import numpy
import matplotlib.pyplot as plot
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

MAX_DATA_POINTS = 200

# TODO: add population growth/decline,
#       population aging,
#       population education,
#       resources available,
#       immigration,
#       population psychological trends,
#       Information dissemination,
#       Cultural Shifts,
#       Technological advancement,
#       Ideological simulation,
#       Natural Disasters,
#       Globalisation


def init_plot():
    figure = plot.figure()

    graph_x_position = 0.1
    graph_y_position = 0.4
    graph_width = 0.8
    graph_height = 0.5
    graph_area = [graph_x_position,
                  graph_y_position, graph_width, graph_height]

    graph = figure.add_axes(graph_area)
    graph.set_title('Population Over Time')
    graph.set_xlabel('Time (Days)')
    graph.set_ylabel('Population')

    return figure, graph


def animate(graph, sliders_with_trendlines):
    graph.clear()
    # Plot trend lines for each slider
    for slider, trend_data in sliders_with_trendlines:

        trend_data['x'].append(len(trend_data['x']))
        trend_data['y'].append(

            # manipulation with your slider value, you can manipulate using functions
            slider.val*numpy.sin(2 * numpy.pi * 0.01 * trend_data['x'][-1] + numpy.pi/4))

        # facilitates continuous graph (last coordinate is deleted to make space for a new one)
        if trend_data['x'][-1] - trend_data['x'][0] > MAX_DATA_POINTS:
            trend_data['x'].pop(0)
            trend_data['y'].pop(0)

        # fills in the area between the point and the x-axis to create an area chart
        graph.fill_between(trend_data['x'], 0, trend_data['y'],
                           label=trend_data['label'], color=trend_data['color'], alpha=0.5)
        graph.autoscale(enable=True, axis='both')
    graph.legend()


def create_animation(figure, animate_func, frames, interval):
    return FuncAnimation(figure, animate_func, frames=frames, interval=interval)


def main():
    figure, graph = init_plot()

    # each frame a new x coordinate is created, probably can be optimised/combined with "MAX_POINTS" logic
    def frames():
        i = 1
        while True:
            yield i
            i += 1

    trend_line_colors = ['r', 'g', 'b']

    number_of_sliders = 3

    # Create a list of sliders with trend lines
    sliders_with_trendlines = []

    slider_height = 0.03
    slider_spacing = 0.04

    # creates the sliders
    for i in range(number_of_sliders):
        graph_slider = plot.axes([0.15, 0.1 + i * (slider_height + slider_spacing),
                                 0.65, slider_height], facecolor='lightgoldenrodyellow')
        slider = Slider(
            graph_slider, f'Slider {i}', 0, 200, valinit=100, valstep=1)
        sliders_with_trendlines.append(
            (slider, {'x': [], 'y': [], 'label': f'Slider {i}', 'color': trend_line_colors[i]}))

    animation = create_animation(figure, lambda args: animate(
        graph, sliders_with_trendlines), frames=frames, interval=100)

    plot.show()


if __name__ == "__main__":
    main()
