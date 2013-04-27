; Auto-generated. Do not edit!


(cl:in-package my_dynamixel_tutorial-srv)


;//! \htmlinclude IkNMotor-request.msg.html

(cl:defclass <IkNMotor-request> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (z
    :reader z
    :initarg :z
    :type cl:float
    :initform 0.0))
)

(cl:defclass IkNMotor-request (<IkNMotor-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <IkNMotor-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'IkNMotor-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name my_dynamixel_tutorial-srv:<IkNMotor-request> is deprecated: use my_dynamixel_tutorial-srv:IkNMotor-request instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <IkNMotor-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader my_dynamixel_tutorial-srv:x-val is deprecated.  Use my_dynamixel_tutorial-srv:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <IkNMotor-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader my_dynamixel_tutorial-srv:y-val is deprecated.  Use my_dynamixel_tutorial-srv:y instead.")
  (y m))

(cl:ensure-generic-function 'z-val :lambda-list '(m))
(cl:defmethod z-val ((m <IkNMotor-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader my_dynamixel_tutorial-srv:z-val is deprecated.  Use my_dynamixel_tutorial-srv:z instead.")
  (z m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <IkNMotor-request>) ostream)
  "Serializes a message object of type '<IkNMotor-request>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <IkNMotor-request>) istream)
  "Deserializes a message object of type '<IkNMotor-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'z) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<IkNMotor-request>)))
  "Returns string type for a service object of type '<IkNMotor-request>"
  "my_dynamixel_tutorial/IkNMotorRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'IkNMotor-request)))
  "Returns string type for a service object of type 'IkNMotor-request"
  "my_dynamixel_tutorial/IkNMotorRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<IkNMotor-request>)))
  "Returns md5sum for a message object of type '<IkNMotor-request>"
  "62de0e2438b033c0a5957a678556e9fd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'IkNMotor-request)))
  "Returns md5sum for a message object of type 'IkNMotor-request"
  "62de0e2438b033c0a5957a678556e9fd")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<IkNMotor-request>)))
  "Returns full string definition for message of type '<IkNMotor-request>"
  (cl:format cl:nil "float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'IkNMotor-request)))
  "Returns full string definition for message of type 'IkNMotor-request"
  (cl:format cl:nil "float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <IkNMotor-request>))
  (cl:+ 0
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <IkNMotor-request>))
  "Converts a ROS message object to a list"
  (cl:list 'IkNMotor-request
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':z (z msg))
))
;//! \htmlinclude IkNMotor-response.msg.html

(cl:defclass <IkNMotor-response> (roslisp-msg-protocol:ros-message)
  ((angles
    :reader angles
    :initarg :angles
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass IkNMotor-response (<IkNMotor-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <IkNMotor-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'IkNMotor-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name my_dynamixel_tutorial-srv:<IkNMotor-response> is deprecated: use my_dynamixel_tutorial-srv:IkNMotor-response instead.")))

(cl:ensure-generic-function 'angles-val :lambda-list '(m))
(cl:defmethod angles-val ((m <IkNMotor-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader my_dynamixel_tutorial-srv:angles-val is deprecated.  Use my_dynamixel_tutorial-srv:angles instead.")
  (angles m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <IkNMotor-response>) ostream)
  "Serializes a message object of type '<IkNMotor-response>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'angles))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'angles))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <IkNMotor-response>) istream)
  "Deserializes a message object of type '<IkNMotor-response>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'angles) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'angles)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<IkNMotor-response>)))
  "Returns string type for a service object of type '<IkNMotor-response>"
  "my_dynamixel_tutorial/IkNMotorResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'IkNMotor-response)))
  "Returns string type for a service object of type 'IkNMotor-response"
  "my_dynamixel_tutorial/IkNMotorResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<IkNMotor-response>)))
  "Returns md5sum for a message object of type '<IkNMotor-response>"
  "62de0e2438b033c0a5957a678556e9fd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'IkNMotor-response)))
  "Returns md5sum for a message object of type 'IkNMotor-response"
  "62de0e2438b033c0a5957a678556e9fd")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<IkNMotor-response>)))
  "Returns full string definition for message of type '<IkNMotor-response>"
  (cl:format cl:nil "float64[] angles~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'IkNMotor-response)))
  "Returns full string definition for message of type 'IkNMotor-response"
  (cl:format cl:nil "float64[] angles~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <IkNMotor-response>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'angles) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <IkNMotor-response>))
  "Converts a ROS message object to a list"
  (cl:list 'IkNMotor-response
    (cl:cons ':angles (angles msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'IkNMotor)))
  'IkNMotor-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'IkNMotor)))
  'IkNMotor-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'IkNMotor)))
  "Returns string type for a service object of type '<IkNMotor>"
  "my_dynamixel_tutorial/IkNMotor")