
(cl:in-package :asdf)

(defsystem "encoder-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "TimeDist" :depends-on ("_package_TimeDist"))
    (:file "_package_TimeDist" :depends-on ("_package"))
  ))