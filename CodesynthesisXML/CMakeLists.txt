#The minimum CMake version which is needed
cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

#Build the actual component
file(GLOB Sources ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp)
file(GLOB GeneratedSourcesXSD ${CMAKE_CURRENT_SOURCE_DIR}/config/*.cxx)
file(GLOB GeneratedHeadersXSD ${CMAKE_CURRENT_SOURCE_DIR}/config/*.hxx)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../
                    ${CONAN_INCLUDE_DIRS})

add_executable(${PROJECT_NAME} ${Sources} ${GeneratedSourcesXSD} ${GeneratedHeadersXSD} )
target_link_libraries(${PROJECT_NAME}
                      ${CONAN_LIBS})
