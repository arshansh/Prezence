execute_process(COMMAND "/home/human/ros_catkin_ws/build/wu_ros_tools/joy_listener/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/human/ros_catkin_ws/build/wu_ros_tools/joy_listener/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
