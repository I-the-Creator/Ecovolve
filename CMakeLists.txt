cmake_minimum_required(VERSION 3.27.2)

project(socio-economics-simulator C)

add_executable(${PROJECT_NAME} src/main.c)
target_link_libraries(${PROJECT_NAME} m)

install(TARGETS ${PROJECT_NAME} DESTINATION bin)
