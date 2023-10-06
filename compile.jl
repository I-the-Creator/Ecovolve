using Pkg

Pkg.activate("./")

using PackageCompiler

create_app("Ecovolve", "EcovolveCompiled", force=true, incremental=true)
