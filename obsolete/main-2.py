import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

MAX_DATA_POINTS = 50


def init_plot():
    fig = plt.figure()

    # Define the size and position of the graph area
    graph_area = [0.1, 0.4, 0.8, 0.5]
    ax1 = fig.add_axes(graph_area)
    ax1.set_title('Population Over Time')
    ax1.set_xlabel('Time (Days)')
    ax1.set_ylabel('Population')

    return fig, ax1


def init_animation_data():
    return [], []

# Function to animate the plot


def animate(args, x, y, ax1, sliders_with_trend):
    x.append(args[0])
    y.append(args[1])

    if len(x) > MAX_DATA_POINTS:
        x.pop(0)
        y.pop(0)

    ax1.clear()
    ax1.fill_between(x, 0, y, color='blue', alpha=0.5)
    ax1.autoscale(enable=True, axis='both')

    # Plot trend lines for each slider
    for slider, trend_data in sliders_with_trend:
        trend_data['x'].append(len(trend_data['x']))
        trend_data['y'].append(slider.val)
        ax1.plot(trend_data['x'], trend_data['y'], linestyle='--',
                 label=trend_data['label'], color=trend_data['color'])
    ax1.legend()

# Function to create and return the animation object


def create_animation(fig, animate_func, frames, interval):
    return FuncAnimation(fig, animate_func, frames=frames, interval=interval)

# Main function


def main():
    fig, ax1 = init_plot()
    x, y = init_animation_data()

    def frames():
        i = 1
        while True:
            yield i, np.random.randint(50, 150)
            i += 1

    # Define the colors for the trend lines
    trend_line_colors = ['r', 'g', 'b']
    num_sliders = len(trend_line_colors)

    # Create a list of sliders with trend lines
    sliders_with_trend = []
    slider_height = 0.03  # Height of each slider
    spacing = 0.04  # Spacing between sliders

    for i in range(num_sliders):
        ax_slider = plt.axes([0.15, 0.1 + i * (slider_height + spacing),
                             0.65, slider_height], facecolor='lightgoldenrodyellow')
        slider = Slider(
            ax_slider, f'Slider {i}', 0, 200, valinit=100, valstep=1)
        sliders_with_trend.append(
            (slider, {'x': [], 'y': [], 'label': f'Slider {i}', 'color': trend_line_colors[i]}))

    ani = create_animation(fig, lambda args: animate(
        args, x, y, ax1, sliders_with_trend), frames=frames, interval=100)

    plt.show()


if __name__ == "__main__":
    main()
