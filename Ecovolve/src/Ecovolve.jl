module Ecovolve
using Gtk, Plots

greet() = print("Hello World!")

function julia_main()::Cint
    try
        main()
    catch
        Base.invokelatest(Base.display_error, Base.catch_stack())
        return 1
    end
    return 0
end

function main()

end

end # module Ecovolve
