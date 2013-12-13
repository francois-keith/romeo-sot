# 
#  Copyright Inria
#
#  Author: François Keith
# 

CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

INCLUDE(cmake/base.cmake)
INCLUDE(cmake/cpack.cmake)

SET(PROJECT_NAME romeo)
SET(PROJECT_DESCRIPTION "Romeo dedicated data files")
SET(PROJECT_URL "https://gforge.inria.fr/projects/romeo-sot/")

set(PROJECT_ROOT_DIR "${CMAKE_CURRENT_SOURCE_DIR}")

SETUP_PROJECT()

ADD_SUBDIRECTORY(include)
ADD_SUBDIRECTORY(data)

SETUP_PROJECT_FINALIZE()
SETUP_PROJECT_CPACK()

