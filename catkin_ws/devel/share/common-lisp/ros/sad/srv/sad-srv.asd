
(cl:in-package :asdf)

(defsystem "sad-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "ImageSrv" :depends-on ("_package_ImageSrv"))
    (:file "_package_ImageSrv" :depends-on ("_package"))
  ))