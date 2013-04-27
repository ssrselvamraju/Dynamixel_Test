/* Auto-generated by genmsg_cpp for file /home/ssr/fuerte_workspace/sandbox/my_dynamixel_tutorial/srv/IkNMotor.srv */
#ifndef MY_DYNAMIXEL_TUTORIAL_SERVICE_IKNMOTOR_H
#define MY_DYNAMIXEL_TUTORIAL_SERVICE_IKNMOTOR_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "ros/service_traits.h"




namespace my_dynamixel_tutorial
{
template <class ContainerAllocator>
struct IkNMotorRequest_ {
  typedef IkNMotorRequest_<ContainerAllocator> Type;

  IkNMotorRequest_()
  : x(0.0)
  , y(0.0)
  , z(0.0)
  {
  }

  IkNMotorRequest_(const ContainerAllocator& _alloc)
  : x(0.0)
  , y(0.0)
  , z(0.0)
  {
  }

  typedef double _x_type;
  double x;

  typedef double _y_type;
  double y;

  typedef double _z_type;
  double z;


  typedef boost::shared_ptr< ::my_dynamixel_tutorial::IkNMotorRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::my_dynamixel_tutorial::IkNMotorRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct IkNMotorRequest
typedef  ::my_dynamixel_tutorial::IkNMotorRequest_<std::allocator<void> > IkNMotorRequest;

typedef boost::shared_ptr< ::my_dynamixel_tutorial::IkNMotorRequest> IkNMotorRequestPtr;
typedef boost::shared_ptr< ::my_dynamixel_tutorial::IkNMotorRequest const> IkNMotorRequestConstPtr;


template <class ContainerAllocator>
struct IkNMotorResponse_ {
  typedef IkNMotorResponse_<ContainerAllocator> Type;

  IkNMotorResponse_()
  : angles()
  {
  }

  IkNMotorResponse_(const ContainerAllocator& _alloc)
  : angles(_alloc)
  {
  }

  typedef std::vector<double, typename ContainerAllocator::template rebind<double>::other >  _angles_type;
  std::vector<double, typename ContainerAllocator::template rebind<double>::other >  angles;


  typedef boost::shared_ptr< ::my_dynamixel_tutorial::IkNMotorResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::my_dynamixel_tutorial::IkNMotorResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct IkNMotorResponse
typedef  ::my_dynamixel_tutorial::IkNMotorResponse_<std::allocator<void> > IkNMotorResponse;

typedef boost::shared_ptr< ::my_dynamixel_tutorial::IkNMotorResponse> IkNMotorResponsePtr;
typedef boost::shared_ptr< ::my_dynamixel_tutorial::IkNMotorResponse const> IkNMotorResponseConstPtr;

struct IkNMotor
{

typedef IkNMotorRequest Request;
typedef IkNMotorResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct IkNMotor
} // namespace my_dynamixel_tutorial

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::my_dynamixel_tutorial::IkNMotorRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::my_dynamixel_tutorial::IkNMotorRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::my_dynamixel_tutorial::IkNMotorRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "4a842b65f413084dc2b10fb484ea7f17";
  }

  static const char* value(const  ::my_dynamixel_tutorial::IkNMotorRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x4a842b65f413084dULL;
  static const uint64_t static_value2 = 0xc2b10fb484ea7f17ULL;
};

template<class ContainerAllocator>
struct DataType< ::my_dynamixel_tutorial::IkNMotorRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "my_dynamixel_tutorial/IkNMotorRequest";
  }

  static const char* value(const  ::my_dynamixel_tutorial::IkNMotorRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::my_dynamixel_tutorial::IkNMotorRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "float64 x\n\
float64 y\n\
float64 z\n\
\n\
";
  }

  static const char* value(const  ::my_dynamixel_tutorial::IkNMotorRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::my_dynamixel_tutorial::IkNMotorRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::my_dynamixel_tutorial::IkNMotorResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::my_dynamixel_tutorial::IkNMotorResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::my_dynamixel_tutorial::IkNMotorResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b7ca77b9da2dfe623a276e10b570d2df";
  }

  static const char* value(const  ::my_dynamixel_tutorial::IkNMotorResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xb7ca77b9da2dfe62ULL;
  static const uint64_t static_value2 = 0x3a276e10b570d2dfULL;
};

template<class ContainerAllocator>
struct DataType< ::my_dynamixel_tutorial::IkNMotorResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "my_dynamixel_tutorial/IkNMotorResponse";
  }

  static const char* value(const  ::my_dynamixel_tutorial::IkNMotorResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::my_dynamixel_tutorial::IkNMotorResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "float64[] angles\n\
\n\
\n\
";
  }

  static const char* value(const  ::my_dynamixel_tutorial::IkNMotorResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::my_dynamixel_tutorial::IkNMotorRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.x);
    stream.next(m.y);
    stream.next(m.z);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct IkNMotorRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::my_dynamixel_tutorial::IkNMotorResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.angles);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct IkNMotorResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<my_dynamixel_tutorial::IkNMotor> {
  static const char* value() 
  {
    return "62de0e2438b033c0a5957a678556e9fd";
  }

  static const char* value(const my_dynamixel_tutorial::IkNMotor&) { return value(); } 
};

template<>
struct DataType<my_dynamixel_tutorial::IkNMotor> {
  static const char* value() 
  {
    return "my_dynamixel_tutorial/IkNMotor";
  }

  static const char* value(const my_dynamixel_tutorial::IkNMotor&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<my_dynamixel_tutorial::IkNMotorRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "62de0e2438b033c0a5957a678556e9fd";
  }

  static const char* value(const my_dynamixel_tutorial::IkNMotorRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<my_dynamixel_tutorial::IkNMotorRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "my_dynamixel_tutorial/IkNMotor";
  }

  static const char* value(const my_dynamixel_tutorial::IkNMotorRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<my_dynamixel_tutorial::IkNMotorResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "62de0e2438b033c0a5957a678556e9fd";
  }

  static const char* value(const my_dynamixel_tutorial::IkNMotorResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<my_dynamixel_tutorial::IkNMotorResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "my_dynamixel_tutorial/IkNMotor";
  }

  static const char* value(const my_dynamixel_tutorial::IkNMotorResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // MY_DYNAMIXEL_TUTORIAL_SERVICE_IKNMOTOR_H
