# 
#  Copyright JRL CNRS-AIST, Inria Rhones-Alpes
#
#  Author: Florent Lamiraux
#          Olivier Stasse
#          Francois Keith
# 

SET(romeo_HEADERS
  romeo/romeo.h 
  romeo-notoes/romeo-notoes.h 
)

#----------------------------------------------------
# Install procedure for the header files
#----------------------------------------------------
INSTALL(FILES ${romeo_HEADERS}
  DESTINATION include/${PROJECT_NAME}
  PERMISSIONS OWNER_READ GROUP_READ WORLD_READ OWNER_WRITE
  )
