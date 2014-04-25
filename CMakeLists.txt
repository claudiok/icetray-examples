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
  private/examples/MutineerTrack.cxx
  USE_PROJECTS icetray dataclasses phys-services
  USE_TOOLS boost python ${OPTIONAL_TOOLS}
  ROOTCINT public/examples/modules/SimpleReconstructionParams.h
  )

i3_add_pybindings(examples
  private/pybindings/module.cxx
  USE_TOOLS boost python 
  USE_PROJECTS icetray dataclasses examples
  )
	
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
  resources/test/passF_fibonacci_is_hiding_at_different_name.py
  resources/test/A0_new_config_syntax.py
  resources/test/A1_pass_i3int_to_module.py
  resources/test/B0_pass_function_to_i3tray.py
  resources/test/B2_pass_closure_to_i3tray.py
  resources/test/B3_filter_with_function.py
  resources/test/D_module_in_python.py
  resources/test/E_module_fancy_parameter_in_python.py
  resources/test/F_use_randomservice.py
  resources/test/G_pass_randomservice_as_param_to_cpp_module.py
  resources/test/I_cpp_uses_python_impl_of_randomservice.py
  ${ROOT_TESTS}
  
  )
