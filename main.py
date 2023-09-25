import numpy
import matplotlib.pyplot as plot
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

MAX_DATA_POINTS = 200


def init_plot():
    figure = plot.figure()

<<<<<<< HEAD
    graph_x_position = 0.1
    graph_y_position = 0.4
    graph_width = 0.8
    graph_height = 0.5
    graph_area = [graph_x_position,
                  graph_y_position, graph_width, graph_height]
=======
    graph_area = [0.1, 0.4, 0.8, 0.5]
    ax1 = fig.add_axes(graph_area)
    ax1.set_title('Population Over Time')
    ax1.set_xlabel('Time (Days)')
    ax1.set_ylabel('Population')
>>>>>>> refs/remotes/origin/main

    graph = figure.add_axes(graph_area)
    graph.set_title('Population Over Time')
    graph.set_xlabel('Time (Days)')
    graph.set_ylabel('Population')

<<<<<<< HEAD
    return figure, graph


def animate(graph, sliders_with_trendlines):
    graph.clear()
    # Plot trend lines for each slider
    for slider, trend_data in sliders_with_trendlines:

        trend_data['x'].append(len(trend_data['x']))
        trend_data['y'].append(
            slider.val*numpy.sin(2 * numpy.pi * 0.01 * trend_data['x'][-1] + numpy.pi/4))
=======

def animate(ax1, sliders_with_trend):
    ax1.clear()
    for slider, trend_data in sliders_with_trend:

        trend_data['x'].append(len(trend_data['x']))
        # trend_data['y'].append(slider.val)
        trend_data['y'].append((1*np.log(2*trend_data['x'][-1]+1))*slider.val*np.sin(2 * np.pi * 0.1 * trend_data['x'][-1] + np.pi/4))
        # trend_data['y'].append(
        #     slider.val*np.sin(2 * np.pi * 0.01 * trend_data['x'][-1] + np.pi/4))
>>>>>>> refs/remotes/origin/main

        if trend_data['x'][-1] - trend_data['x'][0] > MAX_DATA_POINTS:
            trend_data['x'].pop(0)
            trend_data['y'].pop(0)

<<<<<<< HEAD
        graph.fill_between(trend_data['x'], 0, trend_data['y'],
                           label=trend_data['label'], color=trend_data['color'], alpha=0.5)
        graph.autoscale(enable=True, axis='both')
    graph.legend()


def create_animation(figure, animate_func, frames, interval):
    return FuncAnimation(figure, animate_func, frames=frames, interval=interval)


def main():
    figure, graph = init_plot()
=======
        ax1.fill_between(trend_data['x'], 0, trend_data['y'],
                         label=trend_data['label'], color=trend_data['color'], alpha=0.5)
        ax1.autoscale(enable=True, axis='both')
    ax1.legend()


def create_animation(fig, animate_func, frames, interval):
    return FuncAnimation(fig, animate_func, frames=frames, interval=interval)


def main():
    fig, ax1 = init_plot()
>>>>>>> refs/remotes/origin/main

    def frames():
        i = 1
        while True:
            yield i
            i += 1

    trend_line_colors = ['r', 'g', 'b']

    number_of_sliders = 3

<<<<<<< HEAD
    # Create a list of sliders with trend lines
    sliders_with_trendlines = []

    slider_height = 0.03
    slider_spacing = 0.04

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
=======
    sliders_with_trend = []
    slider_height = 0.03
    spacing = 0.04

    for i in range(num_sliders):
        ax_slider = plt.axes([0.15, 0.1 + i * (slider_height + spacing),
                             0.65, slider_height], facecolor='lightgoldenrodyellow')
        slider = Slider(
            ax_slider, f'Slider {i}', 0, 200, valinit=100, valstep=1)
        sliders_with_trend.append(
            (slider, {'x': [], 'y': [], 'label': f'Slider {i}', 'color': trend_line_colors[i]}))

    ani = create_animation(fig, lambda args: animate(
        ax1, sliders_with_trend), frames=frames, interval=100)
>>>>>>> refs/remotes/origin/main



if __name__ == "__main__":
    main()
