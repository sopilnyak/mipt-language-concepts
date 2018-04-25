cmake_minimum_required(VERSION 3.9)
project(vtable)

set(CMAKE_CXX_STANDARD 17)

add_executable(vtable main.cpp)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fpermissive")