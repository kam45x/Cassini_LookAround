cmake_minimum_required(VERSION 3.16)

project(LookAround VERSION 1.0 LANGUAGES CXX)


set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)


find_package(OpenCV REQUIRED)

add_executable(fuzzyfication
        fuzzy_main.cpp
        include/fuzzyfication.hpp
        src/fuzzyfication.cpp
)

# Include directories
target_include_directories(fuzzyfication PRIVATE
    ${OpenCV_INCLUDE_DIRS}
    include
)


target_link_libraries(fuzzyfication PRIVATE ${OpenCV_LIBS})

target_compile_options(fuzzyfication PRIVATE
    -Wall -Wextra -pedantic
)

install(TARGETS fuzzyfication DESTINATION bin)
