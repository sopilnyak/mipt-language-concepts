cmake_minimum_required(VERSION 3.9)
project(exceptions)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fno-exceptions")

add_executable(exceptions main.cpp exceptions.h SafeString.h SafeFile.h BadDestructor.h)
