#include <icetray/I3Frame.h>
#include <icetray/I3Logging.h>
#include <icetray/I3Module.h>

#include <dataclasses/I3Time.h>
#include <dataclasses/I3Double.h>
#include <phys-services/I3RandomService.h>

//
//  Module gets random numbers from a service and puts them into the
//  frame... V2 style.  (See other examples for the v3 style of doing
//  this).
//
class UseRandomV2 : public I3Module
{

  I3RandomServicePtr rs_;
  std::string rs_key_;
  std::string dest_key_;

 public:

  UseRandomV2(const I3Context& ctx)
    : I3Module(ctx)
  {
    AddParameter("I3RandomServiceKey",
		 "my random service location",
		 rs_key_);

    AddParameter("PutWhere",
		 "where the doubles go",
		 dest_key_);

    AddOutBox("OutBox");
  }

  void Configure()
  {
    GetParameter("I3RandomServiceKey", rs_key_);
    GetParameter("PutWhere", dest_key_);

    rs_ = context_.Get<I3RandomServicePtr>(rs_key_);
  }

  void Physics(I3FramePtr frame)
  {
    double d = rs_->Gaus(0, 1);
    I3DoublePtr dp(new I3Double(d));
    frame->Put(dest_key_, dp);
    PushFrame(frame);
  }
    
};

I3_MODULE(UseRandomV2);

