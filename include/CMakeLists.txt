# 
#  Copyright JRL CNRS-AIST
#
#  Author: Florent Lamiraux
#          Olivier Stasse
#          François Keith
# 

SET(romeo_HEADERS
  romeo/romeo.h 
  romeo-notoes/romeo-notoes.h 
)

#----------------------------------------------------
# Install procedure for the header files
#----------------------------------------------------
INSTALL(FILES ${romeo_HEADERS}
  DESTINATION include/
  PERMISSIONS OWNER_READ GROUP_READ WORLD_READ OWNER_WRITE
  )
