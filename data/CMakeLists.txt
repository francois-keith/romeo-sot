# 
#  Copyright CNRS-AIST 
#
#  Author: Florent Lamiraux, François Keith
# 

SET(PROJECT_NAME_NOTOES ${PROJECT_NAME}-notoes)

SET(COMMON_VRML_FILES 
  HeadRoll.wrl        
  LToePitch.wrl       
  RHand.wrl           
  WristYaw.wrl
  LAnkleRoll.wrl      
  LWristPitch.wrl     
  RHipPitch.wrl       
  lankle_romeo_BV.wrl
  LAnkleRollBasic.wrl 
  LWristRoll.wrl      
  RKneePitch.wrl      
  lfoot_romeo_BV.wrl
  LElbowYaw.wrl       
  NeckPitch.wrl       
  RShoulderYaw.wrl    
  ltoe_romeo_BV.wrl
  LHand.wrl           
  Phalax.wrl          
  RThumb.wrl          
  rankle_romeo_BV.wrl
  LHipPitch.wrl       
  PhalaxEnd.wrl       
  RToePitch.wrl       
  rfoot_romeo_BV.wrl
  LKneePitch.wrl      
  RAnkleRoll.wrl      
  RWristPitch.wrl     
  rtoe_romeo_BV.wrl
  LShoulderYaw.wrl    
  RAnkleRollBasic.wrl 
  RWristRoll.wrl
  LThumb.wrl          
  RElbowYaw.wrl       
  Torso.wrl
)

SET(${PROJECT_NAME}_ROMEODATA
  Romeo.wrl
  RomeoLinkJointRank.xml
  RomeoSpecificities.xml
  RomeoInitConfig.dat
  
  RomeoNoToes.wrl
  RomeoNoToesLinkJointRank.xml
  RomeoNoToesSpecificities.xml
  RomeoNoToesInitConfig.dat

  ${COMMON_VRML_FILES}
)

# Install Romeo Current Full specific files

MACRO(INSTALLDATA LPROJECT_NAME)
  MESSAGE(STATUS "INSTALLDATA called for directory: "${LPROJECT_NAME})
  SET(${LPROJECT_NAME}_FULLPATHDATA )
  FOREACH (ldata ${${LPROJECT_NAME}_ROMEODATA})
    SET(${LPROJECT_NAME}_FULLPATHDATA
      ${${LPROJECT_NAME}_FULLPATHDATA} 
      ${CMAKE_CURRENT_SOURCE_DIR}/${ldata})
  ENDFOREACH(ldata)

  INSTALL(FILES ${${LPROJECT_NAME}_FULLPATHDATA}
    DESTINATION share/${LPROJECT_NAME}
    PERMISSIONS OWNER_READ GROUP_READ WORLD_READ OWNER_WRITE
    )
ENDMACRO(INSTALLDATA LPROJECTNAME)

INSTALLDATA(${PROJECT_NAME})
