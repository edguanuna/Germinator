;; Auto-generated. Do not edit!


(when (boundp 'encoder::TimeDist)
  (if (not (find-package "ENCODER"))
    (make-package "ENCODER"))
  (shadow 'TimeDist (find-package "ENCODER")))
(unless (find-package "ENCODER::TIMEDIST")
  (make-package "ENCODER::TIMEDIST"))

(in-package "ROS")
;;//! \htmlinclude TimeDist.msg.html


(defclass encoder::TimeDist
  :super ros::object
  :slots (_timestamp _distanceLeft _distanceRight ))

(defmethod encoder::TimeDist
  (:init
   (&key
    ((:timestamp __timestamp) (instance ros::time :init))
    ((:distanceLeft __distanceLeft) 0.0)
    ((:distanceRight __distanceRight) 0.0)
    )
   (send-super :init)
   (setq _timestamp __timestamp)
   (setq _distanceLeft (float __distanceLeft))
   (setq _distanceRight (float __distanceRight))
   self)
  (:timestamp
   (&optional __timestamp)
   (if __timestamp (setq _timestamp __timestamp)) _timestamp)
  (:distanceLeft
   (&optional __distanceLeft)
   (if __distanceLeft (setq _distanceLeft __distanceLeft)) _distanceLeft)
  (:distanceRight
   (&optional __distanceRight)
   (if __distanceRight (setq _distanceRight __distanceRight)) _distanceRight)
  (:serialization-length
   ()
   (+
    ;; time _timestamp
    8
    ;; float64 _distanceLeft
    8
    ;; float64 _distanceRight
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; time _timestamp
       (write-long (send _timestamp :sec) s) (write-long (send _timestamp :nsec) s)
     ;; float64 _distanceLeft
       (sys::poke _distanceLeft (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _distanceRight
       (sys::poke _distanceRight (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; time _timestamp
     (send _timestamp :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _timestamp :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float64 _distanceLeft
     (setq _distanceLeft (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _distanceRight
     (setq _distanceRight (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get encoder::TimeDist :md5sum-) "3a8d79d031810f535ef4e5c20861539b")
(setf (get encoder::TimeDist :datatype-) "encoder/TimeDist")
(setf (get encoder::TimeDist :definition-)
      "# TimeDist.msg
time timestamp
float64 distanceLeft
float64 distanceRight

")



(provide :encoder/TimeDist "3a8d79d031810f535ef4e5c20861539b")


