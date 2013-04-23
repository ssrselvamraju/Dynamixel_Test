FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../src/my_dynamixel_tutorial/msg"
  "../src/my_dynamixel_tutorial/srv"
  "../msg_gen"
  "../srv_gen"
  "CMakeFiles/rosbuild_premsgsrvgen"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/rosbuild_premsgsrvgen.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
