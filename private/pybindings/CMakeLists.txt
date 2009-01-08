
if(BUILD_PYBINDINGS)
  i3_add_pybindings(examples
    module.cxx
    USE_TOOLS boost python 
    USE_PROJECTS icetray dataclasses examples
    )
endif(BUILD_PYBINDINGS)
