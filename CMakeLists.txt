cmake_minimum_required(VERSION 2.8.3)
project(freeboard_ros)

find_package(catkin REQUIRED roslint)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)


## See http://ros.org/doc/api/catkin/html/user_guide/setup_dot_py.html
#catkin_python_setup()

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES freeboard_ros
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
)

roslint_python()

# TODO: Install
# TODO: Tests
