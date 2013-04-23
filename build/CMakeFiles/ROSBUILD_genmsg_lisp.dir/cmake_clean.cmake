FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../src/my_dynamixel_tutorial/msg"
  "../src/my_dynamixel_tutorial/srv"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_genmsg_lisp"
  "../msg_gen/lisp/xyz.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_xyz.lisp"
  "../msg_gen/lisp/angles.lisp"
  "../msg_gen/lisp/_package.lisp"
  "../msg_gen/lisp/_package_angles.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
