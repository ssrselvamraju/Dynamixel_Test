FILE(REMOVE_RECURSE
  "../msg_gen"
  "../src/my_dynamixel_tutorial/msg"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/my_dynamixel_tutorial/msg/__init__.py"
  "../src/my_dynamixel_tutorial/msg/_xyz.py"
  "../src/my_dynamixel_tutorial/msg/_angles.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
