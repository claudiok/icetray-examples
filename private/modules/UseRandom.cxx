#include <icetray/I3Frame.h>
#include <icetray/I3Logging.h>
#include <icetray/I3Module.h>

#include <dataclasses/I3Time.h>
#include <dataclasses/I3Double.h>
#include <phys-services/I3RandomService.h>

class UseRandom : public I3Module
{
  I3RandomServicePtr rs;
  std::string key;

 public:

  UseRandom(const I3Context& ctx) : I3Module(ctx)
  {
    AddParameter("I3RandomService",
		 "my random service",
		 rs);

    AddParameter("PutWhere",
		 "where the doubles go",
		 key);

    AddOutBox("OutBox");
  }

  void Configure()
  {
    GetParameter("I3RandomService", rs);
    log_debug("rndserv is at %p", rs.get());
    GetParameter("PutWhere", key);
  }

  void Physics(I3FramePtr frame)
  {
    log_debug("rndserv is at %p", rs.get());
    double d = rs->Gaus(0, 1);
    I3DoublePtr dp(new I3Double(d));
    frame->Put(key, dp);
    PushFrame(frame);
  }
};

I3_MODULE(UseRandom);

