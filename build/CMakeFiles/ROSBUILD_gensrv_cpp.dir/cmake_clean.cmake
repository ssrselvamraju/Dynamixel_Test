FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../src/my_dynamixel_tutorial/msg"
  "../src/my_dynamixel_tutorial/srv"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_cpp"
  "../srv_gen/cpp/include/my_dynamixel_tutorial/IkNMotor.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
