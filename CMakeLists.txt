#
# $Id$
#
i3_project(examples
  PYTHON_DIR python
  DOCS_DIR resources/docs)

i3_add_library(examples private/modules/AlmostSmartFeatureExtractor.cxx  
  private/modules/LessDumbFeatureExtractor.cxx
  private/modules/DeltaAngle.cxx			 
  private/modules/NamedFibonacciCheck.cxx
  private/modules/DumbFeatureExtractor.cxx	 
  private/modules/PutParticle.cxx
  private/modules/FibonacciCheck.cxx		 
  private/modules/SimpleReconstruction.cxx
  private/modules/HelloConfiguration.cxx		 
  private/modules/SimpleReconstructionParams.cxx
  private/modules/HelloWorld.cxx			 
  private/modules/Smear.cxx
  private/modules/GetI3Int.cxx
  private/modules/UseRandom.cxx
  private/modules/UseRandomV2.cxx
  private/services/*.cxx 
  private/services/*/*.cxx
  USE_PROJECTS icetray dataclasses phys-services
  USE_TOOLS boost root log4cplus python
  ROOTCINT public/examples/modules/SimpleReconstructionParams.h
  )

add_subdirectory(private/pybindings)

i3_test_scripts(resources/scripts/pass1.py
  resources/scripts/pass2.py
  resources/scripts/pass3.py
  resources/scripts/pass4.py
  resources/scripts/pass4a_delete_unregistered.py
  resources/scripts/pass5.py
  resources/scripts/pass6_HelloWorld.py
  resources/scripts/pass7_HelloConfiguration.py
  resources/scripts/pass7_PutParticle.py
  resources/scripts/pass8_Smear.py
  resources/scripts/pass9_DeltaAngle.py
  resources/scripts/passA_smearing_and_TH1s.py
  resources/scripts/passC_singleton_fibonacci.py
  resources/scripts/passD_singleton_fibonacci_is_a_bad_idea.py
  resources/scripts/passE_one_fibonacci_per_module.py
  resources/scripts/passF_fibonacci_is_hiding_at_different_name.py
  resources/scripts/passG_module_looks_for_fibonacci_in_particular_place.py
  resources/scripts/passH_one_fibonacci_one_module.py
  resources/scripts/passI_verify_not_at_default_location1.py

  python/scripts/A0_new_config_syntax.py
  python/scripts/A1_pass_i3int_to_module.py
  python/scripts/B0_pass_function_to_i3tray.py
  python/scripts/B2_pass_closure_to_i3tray.py
  python/scripts/B3_filter_with_function.py
  python/scripts/D_module_in_python.py
  python/scripts/E_module_fancy_parameter_in_python.py
  python/scripts/F_use_randomservice.py
  python/scripts/G_pass_randomservice_as_param_to_cpp_module.py
  python/scripts/H_pass_randomservice_as_param_to_pymodule.py
  python/scripts/I_cpp_uses_python_impl_of_randomservice.py
  
  python/scripts/K_delang_plot.py
  python/scripts/L_PyLessDumbFeatureExtractor.py
  python/scripts/dom_occupancy.py
  )
