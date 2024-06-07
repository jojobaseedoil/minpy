cmake_minimum_required(VERSION 3.10)
project(minpy)

set(CMAKE_CXX_STANDARD 11)

add_library(minpy SHARED
    source/Multistage.cpp
    source/Slider.cpp
    source/Omega.cpp
)

target_include_directories(minpy PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})