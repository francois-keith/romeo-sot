  CONFIGURE_FILE(
    "${CMAKE_CURRENT_SOURCE_DIR}/robotSpecific_romeo.py.cmake"
    "${CMAKE_CURRENT_BINARY_DIR}/robotSpecific_romeo.py"
    )

  CONFIGURE_FILE(
    "${CMAKE_CURRENT_SOURCE_DIR}/robotSpecific_romeo_notoes.py.cmake"
    "${CMAKE_CURRENT_BINARY_DIR}/robotSpecific_romeo_notoes.py"
    )

  CONFIGURE_FILE(
    "${CMAKE_CURRENT_SOURCE_DIR}/robotSpecific_romeo_hands.py.cmake"
    "${CMAKE_CURRENT_BINARY_DIR}/robotSpecific_romeo_hands.py"
    )

  CONFIGURE_FILE(
    "${CMAKE_CURRENT_SOURCE_DIR}/robotSpecific_romeo_hands_notoes.py.cmake"
    "${CMAKE_CURRENT_BINARY_DIR}/robotSpecific_romeo_hands_notoes.py"
    )

IF(EXISTS ${PROJECT_ROOT_DIR}/../sot-dyninv/python)
INSTALL(FILES
    dyn_romeo_notoes.py
    "${CMAKE_CURRENT_BINARY_DIR}/robotSpecific_romeo.py"
    kinesimple_romeo_notoes.py
    "${CMAKE_CURRENT_BINARY_DIR}/robotSpecific_romeo_notoes.py"
    "${CMAKE_CURRENT_BINARY_DIR}/robotSpecific_romeo_hands.py"
    "${CMAKE_CURRENT_BINARY_DIR}/robotSpecific_romeo_hands_notoes.py"
    DESTINATION ${PROJECT_ROOT_DIR}/../sot-dyninv/python)
ELSE()
# MESSAGE("Impossible to install romeo specific data: the path to sot-dyninv is not known")
ENDIF(EXISTS ${PROJECT_ROOT_DIR}/../sot-dyninv/python)
