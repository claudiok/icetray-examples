#
# $Id$
#
i3_project(examples
  PYTHON_DIR python
  DOCS_DIR resources/docs)

if(USE_ROOT)
  set(OPTIONAL_TOOLS root)
endif(USE_ROOT)

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
  USE_TOOLS boost log4cplus python ${OPTIONAL_TOOLS}
  ROOTCINT public/examples/modules/SimpleReconstructionParams.h
  )

add_subdirectory(private/pybindings)

if(USE_ROOT)
  set(ROOT_TESTS 
	resources/test/pass9_DeltaAngle.py
	resources/test/passA_smearing_and_TH1s.py
  )
endif(USE_ROOT)

i3_test_scripts(resources/test/pass1.py
  resources/test/pass2.py
  resources/test/pass3.py
  resources/test/pass4.py
  resources/test/pass4a_delete_unregistered.py
  resources/test/pass5.py
  resources/test/pass6_HelloWorld.py
  resources/test/pass7_HelloConfiguration.py
  resources/test/pass7_PutParticle.py
  resources/test/pass8_Smear.py
  resources/test/passC_singleton_fibonacci.py
  resources/test/passD_singleton_fibonacci_is_a_bad_idea.py
  resources/test/passE_one_fibonacci_per_module.py
  resources/test/passF_fibonacci_is_hiding_at_different_name.py
  resources/test/passG_module_looks_for_fibonacci_in_particular_place.py
  resources/test/passH_one_fibonacci_one_module.py
  resources/test/passI_verify_not_at_default_location1.py
  ${ROOT_TESTS}

  python/scripts/A0_new_config_syntax.py
  python/scripts/A1_pass_i3int_to_module.py
  python/scripts/B0_pass_function_to_i3tray.py
  python/scripts/B2_pass_closure_to_i3tray.py
  python/scripts/B3_filter_with_function.py
  python/scripts/D_module_in_python.py
  python/scripts/E_module_fancy_parameter_in_python.py
  python/scripts/F_use_randomservice.py
  python/scripts/G_pass_randomservice_as_param_to_cpp_module.py
  python/scripts/I_cpp_uses_python_impl_of_randomservice.py
  
  )
