/**
 *  $Id$
 *  
 *  Copyright (C) 2007   Troy D. Straszheim  <troy@icecube.umd.edu>
 *  and the IceCube Collaboration <http://www.icecube.wisc.edu>
 *  
 *  This file is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 3 of the License, or
 *  (at your option) any later version.
 *  
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *  
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>
 *  
 */
#include <icetray/I3Module.h>
#include <icetray/Utility.h>
#include <icetray/I3Frame.h>
#include <icetray/I3Int.h>

#include <string>
#include <set>

class GetI3Int : public I3Module
{
public:

  GetI3Int (const I3Context& context);
  void Configure();
  void Process() { }
};

I3_MODULE(GetI3Int);

using namespace std;

GetI3Int::GetI3Int(const I3Context& context) : I3Module(context)
{
  AddParameter("obj", "i can take a python-wrapped C++ class as a parameter", "(nil)");
}

void
GetI3Int::Configure()
{
  I3IntPtr ip;
  GetParameter("obj", ip);
  std::cout << "I got int value=" << ip->value << "\n";
}


