#include <examples/modules/HelloWorld.h>
#include <icetray/I3Frame.h>
#include <icetray/I3FrameObject.h>
#include <icetray/OMKey.h>
#include <icetray/I3Context.h>
#include <icetray/I3Configuration.h>
#include <dataclasses/I3String.h>

#include <dataclasses/physics/I3Particle.h>

#include <TFile.h>
#include <TTree.h>

using namespace std;

// This is necessary, it registers the module's existence with the
// framework.
I3_MODULE(HelloWorld);


HelloWorld::HelloWorld(const I3Context& context) : 
  I3Module(context), 
  where_("Hello"),   // default values
  say_what_("World") 
{
  // tell the framework that we have an outbox...
  AddOutBox("OutBox");

  // tell the framework that we have one parameter named Where.
  // this also sets the default value.
  AddParameter("Where", "Where to say hello.", where_);
  AddParameter("SayWhat", "What to say.", say_what_);
}

void HelloWorld::Configure()
{
  // Get the value the user set in the steering file
  GetParameter("Where", where_);
  GetParameter("SayWhat", say_what_);
}

void 
HelloWorld::Physics(I3FramePtr frame)
{
  // Say Hello!

  // create a shared pointer to a new I3String
  I3StringPtr string_p(new I3String);

  // set the value 
  string_p->value = say_what_;

  // put it in the frame...
  frame->Put(where_, string_p);

  // send the frame downstream.
  PushFrame(frame,"OutBox");
}

