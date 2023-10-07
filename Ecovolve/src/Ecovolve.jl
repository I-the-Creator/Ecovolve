module Ecovolve
using Gtk
using GtkReactive
using Plots
inspectdr()

function main()
    window = GtkWindow("Julia GTK App", 800, 600)

    verticalBox = GtkBox(:v)
    add(window, verticalBox)

    sliderAmplitude = GtkScale(0.1, 5.0, 0.1)
    sliderFrequency = GtkScale(1.0, 10.0, 0.1)
    sliderPhase = GtkScale(0.0, 2π, 0.1)

    Graph = GtkDrawingArea()

    plot = plot([], [], xlabel="X", ylabel="Y", legend=false)

    function update_graph()
        amplitude = sliderAmplitude.value
        frequency = sliderFrequency.value
        phase = sliderPhase.value

        x = 0:0.1:10  # Define x values
        y = amplitude * sin.(frequency * x .+ phase)  # Calculate y values

        # Update the plot data
        plot[1] = x
        plot[2] = y

        # Redraw the plot
        display(Graph)
    end

    # Connect the sliders to the update function
    signal_connect(sliderAmplitude, :value, update_graph)
    signal_connect(sliderFrequency, :value, update_graph)
    signal_connect(sliderPhase, :value, update_graph)

    # Add widgets to the main window layout
    GtkBox.add(verticalBox, sliderAmplitude)
    GtkBox.add(verticalBox, sliderFrequency)
    GtkBox.add(verticalBox, sliderPhase)
    GtkBox.add(verticalBox, Graph)

    # Show the window
    showall(window)

    # Start the GTK main loop
    Gtk.main()
end

function julia_main()::Cint
    try
        main()
    catch
        Base.invokelatest(Base.display_error, Base.catch_stack())
        return 1
    end
    return 0
end
end # module Ecovolve
