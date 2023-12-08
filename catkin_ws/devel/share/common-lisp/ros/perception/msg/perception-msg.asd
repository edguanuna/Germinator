
(cl:in-package :asdf)

(defsystem "perception-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "CentroidsArray" :depends-on ("_package_CentroidsArray"))
    (:file "_package_CentroidsArray" :depends-on ("_package"))
  ))