
(cl:in-package :asdf)

(defsystem "my_dynamixel_tutorial-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "IkNMotor" :depends-on ("_package_IkNMotor"))
    (:file "_package_IkNMotor" :depends-on ("_package"))
  ))