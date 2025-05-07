cmake_minimum_required(VERSION 3.22)
project(EHM)

find_package(Eigen3 REQUIRED)


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
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  PRIVATE
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include/EHM>
  ${EIGEN3_INCLUDE_DIR}
)
