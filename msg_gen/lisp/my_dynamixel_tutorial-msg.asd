
(cl:in-package :asdf)

(defsystem "my_dynamixel_tutorial-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "xyz" :depends-on ("_package_xyz"))
    (:file "_package_xyz" :depends-on ("_package"))
    (:file "angles" :depends-on ("_package_angles"))
    (:file "_package_angles" :depends-on ("_package"))
  ))