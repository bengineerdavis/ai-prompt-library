cmake_minimum_required(VERSION 3.20)
project(cmake-demo C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

add_executable(cmake-demo src/main.c)
