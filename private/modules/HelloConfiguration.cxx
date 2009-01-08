#include <examples/modules/HelloConfiguration.h>
#include <icetray/I3Frame.h>
#include <icetray/I3FrameObject.h>
#include <icetray/OMKey.h>
#include <icetray/I3Context.h>
#include <icetray/I3Configuration.h>
#include <dataclasses/I3String.h>

#include <dataclasses/physics/I3Particle.h>

using namespace std;

I3_MODULE(HelloConfiguration);


HelloConfiguration::HelloConfiguration(const I3Context& context) : 
  I3Module(context)
{
  // tell the framework that we have an outbox...
  AddOutBox("OutBox");

  // "add" each parameter.  It's identifier, then descriptive string,
  // then the variable.  Don't skimp on your descriptive strings.
  // They get recorded in the .i3 file and are helpful later.
  
  an_int_ = 2;
  AddParameter("mtgs/yr", 
	       "Number of collaboration meetings per year", 
	       an_int_);

  a_bool_ = false;
  AddParameter("naps", 
	       "Allow naps during plenary sessions", 
	       a_bool_);

  AddParameter("COG", 
	       "Use this OM as the center of gravity for the Haystack Fit.", 
	       an_omkey_);

  a_double_ = 0.0000001;
  AddParameter("PeekFactor", 
	       "Likelihood reconstruction will peek at MC", 
	       a_double_);

  a_string_ = "Outsmarting wall streeters on the internet with a perl script.";
  AddParameter("Rather", 
	       "What you'd rather be doing", 
	       a_string_);

  AddParameter("vector_of_ints", 
	       "What this vector of ints means to this module.", 
	       vector_of_ints_);

  AddParameter("vector_of_ulongs", 
	       "What this vector of ints means to this module.", 
	       vector_of_ulongs_);

  AddParameter("vector_of_doubles", 
	       "How this module will change its behavior depending on these doubles.", 
	       vector_of_doubles_);

  AddParameter("vector_of_omkeys", 
	       "These are the OMs named Brian.", 
	       vector_of_omkeys_);

  AddParameter("vector_of_strings", 
	       "A sentence describing the parameter \"vector_of_strings\".", 
	       vector_of_strings_);
}

void HelloConfiguration::Configure()
{
  // this fetches the configured values from the steering file and
  // puts them into the local variables.
  GetParameter("mtgs/yr", an_int_);
  GetParameter("naps", a_bool_);
  GetParameter("COG", an_omkey_);
  //
  // notice that parameter names are insensitive: they get stored
  // internally as all-lowercase and anytime you add/get/set one, case
  // is ignored.  We added this one as 'PeekFactor', for instance:
  //
  GetParameter("PeEkFaCtOr", a_double_);
  GetParameter("rather", a_string_);

  GetParameter("vector_of_ints", vector_of_ints_);
  GetParameter("vector_of_ulongs", vector_of_ulongs_);
  GetParameter("vector_of_doubles", vector_of_doubles_);
  GetParameter("vector_of_omkeys", vector_of_omkeys_);
  GetParameter("vector_of_strings", vector_of_strings_);
}

void 
HelloConfiguration::Physics(I3FramePtr frame)
{

  // This is a configuration demo, not a putting things in the frame
  // demo.  Run the module and look at the configuration stored in the
  // .i3 file.

  // send the frame downstream.
  PushFrame(frame,"OutBox");
}

