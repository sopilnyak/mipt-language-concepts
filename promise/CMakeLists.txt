cmake_minimum_required(VERSION 3.9)
project(promise)

set(CMAKE_CXX_STANDARD 11)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread")

add_executable(promise main.cpp Future.h Data.h Promise.h)