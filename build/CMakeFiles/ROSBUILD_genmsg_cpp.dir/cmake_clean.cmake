FILE(REMOVE_RECURSE
  "../msg_gen"
  "../src/my_dynamixel_tutorial/msg"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_cpp"
  "../msg_gen/cpp/include/my_dynamixel_tutorial/xyz.h"
  "../msg_gen/cpp/include/my_dynamixel_tutorial/angles.h"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_cpp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
