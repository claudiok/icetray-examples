#include <examples/modules/FibonacciCheck.h>
#include <examples/services/SequenceService.h>

#include <icetray/I3Frame.h>
#include <icetray/I3Context.h>

using namespace std;

I3_MODULE(FibonacciCheck);


FibonacciCheck::FibonacciCheck(const I3Context& context) : 
  I3Module(context)
{
  prev_=0;
  prev_prev_=0;
  // tell the framework that we have an outbox...
  AddOutBox("OutBox");
}

void 
FibonacciCheck::Configure()
{

}

void 
FibonacciCheck::Physics(I3FramePtr frame)
{
  // get a reference to whatever sequence service the icetray has put
  // at my disposal
  SequenceService& seq = context_.Get<SequenceService>();

  // get the next fibonacci number
  unsigned fib = seq.next();
  
  // if we're past the special cases at 0 and 1, make sure it is equal
  // to the sum of the previous two
  if (fib >= 2 && fib != prev_ + prev_prev_)
    log_fatal("Fibonacci # incorrect.  I expected %u, but I got %u.", 
	      prev_ + prev_prev_,
	      fib);

  log_info("Next fibonacci # is %u", fib);
  // shift our small history
  prev_prev_ = prev_;
  prev_ = fib;

  // send the frame downstream.
  PushFrame(frame,"OutBox");
}

