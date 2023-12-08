; Auto-generated. Do not edit!


(cl:in-package encoder-msg)


;//! \htmlinclude TimeDist.msg.html

(cl:defclass <TimeDist> (roslisp-msg-protocol:ros-message)
  ((timestamp
    :reader timestamp
    :initarg :timestamp
    :type cl:real
    :initform 0)
   (distanceLeft
    :reader distanceLeft
    :initarg :distanceLeft
    :type cl:float
    :initform 0.0)
   (distanceRight
    :reader distanceRight
    :initarg :distanceRight
    :type cl:float
    :initform 0.0))
)

(cl:defclass TimeDist (<TimeDist>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TimeDist>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TimeDist)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name encoder-msg:<TimeDist> is deprecated: use encoder-msg:TimeDist instead.")))

(cl:ensure-generic-function 'timestamp-val :lambda-list '(m))
(cl:defmethod timestamp-val ((m <TimeDist>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader encoder-msg:timestamp-val is deprecated.  Use encoder-msg:timestamp instead.")
  (timestamp m))

(cl:ensure-generic-function 'distanceLeft-val :lambda-list '(m))
(cl:defmethod distanceLeft-val ((m <TimeDist>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader encoder-msg:distanceLeft-val is deprecated.  Use encoder-msg:distanceLeft instead.")
  (distanceLeft m))

(cl:ensure-generic-function 'distanceRight-val :lambda-list '(m))
(cl:defmethod distanceRight-val ((m <TimeDist>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader encoder-msg:distanceRight-val is deprecated.  Use encoder-msg:distanceRight instead.")
  (distanceRight m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TimeDist>) ostream)
  "Serializes a message object of type '<TimeDist>"
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'timestamp)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'timestamp) (cl:floor (cl:slot-value msg 'timestamp)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'distanceLeft))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'distanceRight))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TimeDist>) istream)
  "Deserializes a message object of type '<TimeDist>"
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'timestamp) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'distanceLeft) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'distanceRight) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TimeDist>)))
  "Returns string type for a message object of type '<TimeDist>"
  "encoder/TimeDist")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TimeDist)))
  "Returns string type for a message object of type 'TimeDist"
  "encoder/TimeDist")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TimeDist>)))
  "Returns md5sum for a message object of type '<TimeDist>"
  "3a8d79d031810f535ef4e5c20861539b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TimeDist)))
  "Returns md5sum for a message object of type 'TimeDist"
  "3a8d79d031810f535ef4e5c20861539b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TimeDist>)))
  "Returns full string definition for message of type '<TimeDist>"
  (cl:format cl:nil "# TimeDist.msg~%time timestamp~%float64 distanceLeft~%float64 distanceRight~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TimeDist)))
  "Returns full string definition for message of type 'TimeDist"
  (cl:format cl:nil "# TimeDist.msg~%time timestamp~%float64 distanceLeft~%float64 distanceRight~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TimeDist>))
  (cl:+ 0
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TimeDist>))
  "Converts a ROS message object to a list"
  (cl:list 'TimeDist
    (cl:cons ':timestamp (timestamp msg))
    (cl:cons ':distanceLeft (distanceLeft msg))
    (cl:cons ':distanceRight (distanceRight msg))
))
