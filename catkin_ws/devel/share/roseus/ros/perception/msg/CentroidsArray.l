;; Auto-generated. Do not edit!


(when (boundp 'perception::CentroidsArray)
  (if (not (find-package "PERCEPTION"))
    (make-package "PERCEPTION"))
  (shadow 'CentroidsArray (find-package "PERCEPTION")))
(unless (find-package "PERCEPTION::CENTROIDSARRAY")
  (make-package "PERCEPTION::CENTROIDSARRAY"))

(in-package "ROS")
;;//! \htmlinclude CentroidsArray.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass perception::CentroidsArray
  :super ros::object
  :slots (_header _centroids ))

(defmethod perception::CentroidsArray
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:centroids __centroids) ())
    )
   (send-super :init)
   (setq _header __header)
   (setq _centroids __centroids)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:centroids
   (&rest __centroids)
   (if (keywordp (car __centroids))
       (send* _centroids __centroids)
     (progn
       (if __centroids (setq _centroids (car __centroids)))
       _centroids)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; geometry_msgs/Point[] _centroids
    (apply #'+ (send-all _centroids :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; geometry_msgs/Point[] _centroids
     (write-long (length _centroids) s)
     (dolist (elem _centroids)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; geometry_msgs/Point[] _centroids
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _centroids (let (r) (dotimes (i n) (push (instance geometry_msgs::Point :init) r)) r))
     (dolist (elem- _centroids)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get perception::CentroidsArray :md5sum-) "6fdfa26afed9c608e923375eed94abe0")
(setf (get perception::CentroidsArray :datatype-) "perception/CentroidsArray")
(setf (get perception::CentroidsArray :definition-)
      "# File: perception/msg/CentroidsArray.msg
Header header
geometry_msgs/Point[] centroids

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

")



(provide :perception/CentroidsArray "6fdfa26afed9c608e923375eed94abe0")


