cmake_minimum_required(VERSION 3.22)
project(EHM)

# find dependencies
find_package(Eigen3 REQUIRED)


# # Create a include folder in the build directory
# file(MAKE_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/EHM)
# # Copy .h files using glob pattern into the build directory keeping the folder structure
# file(GLOB_RECURSE EHM_HEADERS ${CMAKE_CURRENT_SOURCE_DIR}/src/*.h)
# foreach(EHM_HEADER ${EHM_HEADERS})
#     file(RELATIVE_PATH REL_HEADER ${CMAKE_CURRENT_SOURCE_DIR}/src ${EHM_HEADER})
#     get_filename_component(REL_HEADER_PATH ${REL_HEADER} PATH)
#     file(MAKE_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/EHM/${REL_HEADER_PATH})
#     configure_file(${EHM_HEADER} ${CMAKE_CURRENT_SOURCE_DIR}/include/EHM/${REL_HEADER} COPYONLY)
# endforeach()

add_library(EHM
    STATIC
    src/core/EHM2.cpp
    src/core/EHM.cpp
    src/net/EHM2Net.cpp
    src/net/EHMNet.cpp
    src/net/EHM2NetNode.cpp
    src/net/EHMNetNode.cpp
    src/net/EHM2Tree.cpp
    src/utils/Cluster.cpp
    src/utils/Utils.cpp
)
target_include_directories(
  EHM
  SYSTEM PUBLIC
  $<INSTALL_INTERFACE:include>
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include/EHM>
  PRIVATE
  ${EIGEN3_INCLUDE_DIR}
)