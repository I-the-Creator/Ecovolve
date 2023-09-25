import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# Constants
MAX_DATA_POINTS = 200

# Function to initialize the plot
def init_plot():
    fig = plt.figure()

    # Define the size and position of the graph area
    graph_area = [0.1, 0.4, 0.8, 0.5]
    ax1 = fig.add_axes(graph_area)
    ax1.set_title('Population Over Time')
    ax1.set_xlabel('Time (Days)')
    ax1.set_ylabel('Population')

    return fig, ax1

# Function to animate the plot
def animate(ax1, sliders_with_trend):
    ax1.clear()
    # Plot trend lines for each slider
    for slider, trend_data in sliders_with_trend:
        
        trend_data['x'].append(len(trend_data['x']))
        # trend_data['y'].append(slider.val)
        # trend_data['y'].append((1*np.log(2*trend_data['x'][-1]+1))*slider.val*np.sin(2 * np.pi * 1 * trend_data['x'][-1] + np.pi/4))
        trend_data['y'].append(slider.val*np.sin(2 * np.pi * 0.01 * trend_data['x'][-1] + np.pi/4))
        
        if trend_data['x'][-1] - trend_data['x'][0] > MAX_DATA_POINTS:
            trend_data['x'].pop(0)
            trend_data['y'].pop(0)
        
        ax1.fill_between(trend_data['x'], 0, trend_data['y'], label=trend_data['label'], color=trend_data['color'], alpha=0.5)
        ax1.autoscale(enable=True, axis='both')
    ax1.legend()

# Function to create and return the animation object
def create_animation(fig, animate_func, frames, interval):
    return FuncAnimation(fig, animate_func, frames=frames, interval=interval)

# Main function
def main():
    fig, ax1 = init_plot()

    def frames():
        i = 1
        while True:
            yield i
            i += 1

    # Define the colors for the trend lines
    trend_line_colors = ['r', 'g', 'b']
    num_sliders = len(trend_line_colors)

    # Create a list of sliders with trend lines
    sliders_with_trend = []
    slider_height = 0.03  # Height of each slider
    spacing = 0.04  # Spacing between sliders

    for i in range(num_sliders):
        ax_slider = plt.axes([0.15, 0.1 + i * (slider_height + spacing), 0.65, slider_height], facecolor='lightgoldenrodyellow')
        slider = Slider(ax_slider, f'Slider {i}', 0, 200, valinit=100, valstep=1)
        sliders_with_trend.append((slider, {'x': [], 'y': [], 'label': f'Slider {i}', 'color': trend_line_colors[i]}))

    ani = create_animation(fig, lambda args: animate(ax1, sliders_with_trend), frames=frames, interval=100)

    plt.show()

if __name__ == "__main__":
    main()
