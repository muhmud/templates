project(test_project)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_compile_options(-std=c++11)

add_executable(testing project/src/main.cpp)
target_link_libraries(testing ${CONAN_LIBS})
