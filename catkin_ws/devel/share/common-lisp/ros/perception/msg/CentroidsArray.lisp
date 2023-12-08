; Auto-generated. Do not edit!


(cl:in-package perception-msg)


;//! \htmlinclude CentroidsArray.msg.html

(cl:defclass <CentroidsArray> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (centroids
    :reader centroids
    :initarg :centroids
    :type (cl:vector geometry_msgs-msg:Point)
   :initform (cl:make-array 0 :element-type 'geometry_msgs-msg:Point :initial-element (cl:make-instance 'geometry_msgs-msg:Point))))
)

(cl:defclass CentroidsArray (<CentroidsArray>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CentroidsArray>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CentroidsArray)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name perception-msg:<CentroidsArray> is deprecated: use perception-msg:CentroidsArray instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <CentroidsArray>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader perception-msg:header-val is deprecated.  Use perception-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'centroids-val :lambda-list '(m))
(cl:defmethod centroids-val ((m <CentroidsArray>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader perception-msg:centroids-val is deprecated.  Use perception-msg:centroids instead.")
  (centroids m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CentroidsArray>) ostream)
  "Serializes a message object of type '<CentroidsArray>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'centroids))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'centroids))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CentroidsArray>) istream)
  "Deserializes a message object of type '<CentroidsArray>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'centroids) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'centroids)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'geometry_msgs-msg:Point))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CentroidsArray>)))
  "Returns string type for a message object of type '<CentroidsArray>"
  "perception/CentroidsArray")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CentroidsArray)))
  "Returns string type for a message object of type 'CentroidsArray"
  "perception/CentroidsArray")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CentroidsArray>)))
  "Returns md5sum for a message object of type '<CentroidsArray>"
  "6fdfa26afed9c608e923375eed94abe0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CentroidsArray)))
  "Returns md5sum for a message object of type 'CentroidsArray"
  "6fdfa26afed9c608e923375eed94abe0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CentroidsArray>)))
  "Returns full string definition for message of type '<CentroidsArray>"
  (cl:format cl:nil "# File: perception/msg/CentroidsArray.msg~%Header header~%geometry_msgs/Point[] centroids~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CentroidsArray)))
  "Returns full string definition for message of type 'CentroidsArray"
  (cl:format cl:nil "# File: perception/msg/CentroidsArray.msg~%Header header~%geometry_msgs/Point[] centroids~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CentroidsArray>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'centroids) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CentroidsArray>))
  "Converts a ROS message object to a list"
  (cl:list 'CentroidsArray
    (cl:cons ':header (header msg))
    (cl:cons ':centroids (centroids msg))
))
