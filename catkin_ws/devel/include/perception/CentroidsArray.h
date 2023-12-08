// Generated by gencpp from file perception/CentroidsArray.msg
// DO NOT EDIT!


#ifndef PERCEPTION_MESSAGE_CENTROIDSARRAY_H
#define PERCEPTION_MESSAGE_CENTROIDSARRAY_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <geometry_msgs/Point.h>

namespace perception
{
template <class ContainerAllocator>
struct CentroidsArray_
{
  typedef CentroidsArray_<ContainerAllocator> Type;

  CentroidsArray_()
    : header()
    , centroids()  {
    }
  CentroidsArray_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , centroids(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef std::vector< ::geometry_msgs::Point_<ContainerAllocator> , typename std::allocator_traits<ContainerAllocator>::template rebind_alloc< ::geometry_msgs::Point_<ContainerAllocator> >> _centroids_type;
  _centroids_type centroids;





  typedef boost::shared_ptr< ::perception::CentroidsArray_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::perception::CentroidsArray_<ContainerAllocator> const> ConstPtr;

}; // struct CentroidsArray_

typedef ::perception::CentroidsArray_<std::allocator<void> > CentroidsArray;

typedef boost::shared_ptr< ::perception::CentroidsArray > CentroidsArrayPtr;
typedef boost::shared_ptr< ::perception::CentroidsArray const> CentroidsArrayConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::perception::CentroidsArray_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::perception::CentroidsArray_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::perception::CentroidsArray_<ContainerAllocator1> & lhs, const ::perception::CentroidsArray_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.centroids == rhs.centroids;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::perception::CentroidsArray_<ContainerAllocator1> & lhs, const ::perception::CentroidsArray_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace perception

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::perception::CentroidsArray_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::perception::CentroidsArray_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::perception::CentroidsArray_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::perception::CentroidsArray_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::perception::CentroidsArray_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::perception::CentroidsArray_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::perception::CentroidsArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6fdfa26afed9c608e923375eed94abe0";
  }

  static const char* value(const ::perception::CentroidsArray_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6fdfa26afed9c608ULL;
  static const uint64_t static_value2 = 0xe923375eed94abe0ULL;
};

template<class ContainerAllocator>
struct DataType< ::perception::CentroidsArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "perception/CentroidsArray";
  }

  static const char* value(const ::perception::CentroidsArray_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::perception::CentroidsArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# File: perception/msg/CentroidsArray.msg\n"
"Header header\n"
"geometry_msgs/Point[] centroids\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
;
  }

  static const char* value(const ::perception::CentroidsArray_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::perception::CentroidsArray_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.centroids);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CentroidsArray_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::perception::CentroidsArray_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::perception::CentroidsArray_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "centroids[]" << std::endl;
    for (size_t i = 0; i < v.centroids.size(); ++i)
    {
      s << indent << "  centroids[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::geometry_msgs::Point_<ContainerAllocator> >::stream(s, indent + "    ", v.centroids[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // PERCEPTION_MESSAGE_CENTROIDSARRAY_H