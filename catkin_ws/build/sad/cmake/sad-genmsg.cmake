# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "sad: 0 messages, 1 services")

set(MSG_I_FLAGS "-Isensor_msgs:/opt/ros/noetic/share/sensor_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(sad_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/germinator/Germinator/catkin_ws/src/sad/srv/ImageSrv.srv" NAME_WE)
add_custom_target(_sad_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "sad" "/home/germinator/Germinator/catkin_ws/src/sad/srv/ImageSrv.srv" "std_msgs/Header:sensor_msgs/Image"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(sad
  "/home/germinator/Germinator/catkin_ws/src/sad/srv/ImageSrv.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/sensor_msgs/cmake/../msg/Image.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sad
)

### Generating Module File
_generate_module_cpp(sad
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sad
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(sad_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(sad_generate_messages sad_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/germinator/Germinator/catkin_ws/src/sad/srv/ImageSrv.srv" NAME_WE)
add_dependencies(sad_generate_messages_cpp _sad_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sad_gencpp)
add_dependencies(sad_gencpp sad_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sad_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(sad
  "/home/germinator/Germinator/catkin_ws/src/sad/srv/ImageSrv.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/sensor_msgs/cmake/../msg/Image.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sad
)

### Generating Module File
_generate_module_eus(sad
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sad
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(sad_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(sad_generate_messages sad_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/germinator/Germinator/catkin_ws/src/sad/srv/ImageSrv.srv" NAME_WE)
add_dependencies(sad_generate_messages_eus _sad_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sad_geneus)
add_dependencies(sad_geneus sad_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sad_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(sad
  "/home/germinator/Germinator/catkin_ws/src/sad/srv/ImageSrv.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/sensor_msgs/cmake/../msg/Image.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sad
)

### Generating Module File
_generate_module_lisp(sad
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sad
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(sad_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(sad_generate_messages sad_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/germinator/Germinator/catkin_ws/src/sad/srv/ImageSrv.srv" NAME_WE)
add_dependencies(sad_generate_messages_lisp _sad_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sad_genlisp)
add_dependencies(sad_genlisp sad_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sad_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(sad
  "/home/germinator/Germinator/catkin_ws/src/sad/srv/ImageSrv.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/sensor_msgs/cmake/../msg/Image.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sad
)

### Generating Module File
_generate_module_nodejs(sad
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sad
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(sad_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(sad_generate_messages sad_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/germinator/Germinator/catkin_ws/src/sad/srv/ImageSrv.srv" NAME_WE)
add_dependencies(sad_generate_messages_nodejs _sad_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sad_gennodejs)
add_dependencies(sad_gennodejs sad_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sad_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(sad
  "/home/germinator/Germinator/catkin_ws/src/sad/srv/ImageSrv.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/sensor_msgs/cmake/../msg/Image.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sad
)

### Generating Module File
_generate_module_py(sad
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sad
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(sad_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(sad_generate_messages sad_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/germinator/Germinator/catkin_ws/src/sad/srv/ImageSrv.srv" NAME_WE)
add_dependencies(sad_generate_messages_py _sad_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(sad_genpy)
add_dependencies(sad_genpy sad_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS sad_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sad)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/sad
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET sensor_msgs_generate_messages_cpp)
  add_dependencies(sad_generate_messages_cpp sensor_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sad)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/sad
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET sensor_msgs_generate_messages_eus)
  add_dependencies(sad_generate_messages_eus sensor_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sad)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/sad
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET sensor_msgs_generate_messages_lisp)
  add_dependencies(sad_generate_messages_lisp sensor_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sad)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/sad
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET sensor_msgs_generate_messages_nodejs)
  add_dependencies(sad_generate_messages_nodejs sensor_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sad)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sad\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/sad
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET sensor_msgs_generate_messages_py)
  add_dependencies(sad_generate_messages_py sensor_msgs_generate_messages_py)
endif()
