project(my_project)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_compile_options(-std=c++11)

include_directories(src)

add_executable(app src/main.cpp)
target_link_libraries(app ${CONAN_LIBS})
