  CONFIGURE_FILE(
    "${CMAKE_CURRENT_SOURCE_DIR}/robotSpecific_romeo.py.cmake"
    "${CMAKE_CURRENT_BINARY_DIR}/robotSpecific_romeo.py"
    )

  CONFIGURE_FILE(
    "${CMAKE_CURRENT_SOURCE_DIR}/robotSpecific_romeo_notoes.py.cmake"
    "${CMAKE_CURRENT_BINARY_DIR}/robotSpecific_romeo_notoes.py"
    )
