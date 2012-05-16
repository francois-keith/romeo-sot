# --- ROBOT CONFIG -------------------------------------------------------------
from robotSpecific import pkgDataRootDir,modelName,robotDimension,initialConfig,gearRatio,inertiaRotor,specificitiesName,jointRankName

# RomeoHandsNoToes data
pkgDataRootDir['romeo_hands_notoes'] = "${CMAKE_INSTALL_PREFIX}/share/romeo"
modelName['romeo_hands_notoes'] = 'RomeoHandsNoToes.wrl'
specificitiesName['romeo_hands_notoes'] = 'RomeoHandsNoToesSpecificities.xml'
jointRankName['romeo_hands_notoes'] = 'RomeoHandsNoToesLinkJointRank.xml'
robotDimension['romeo_hands_notoes'] = 61
initialConfig['romeo_hands_notoes'] = (
0, 0, 0.840252, 0, 0, 0, 		 # FF 
0, 		 # chest      
0, 0, 0, 0, 		 # head       
1.5, 0.6, -0.5, -1.05, -0.4, -0.3, -0.2, 		 # left arm   
1.5, -0.6, 0.5, 1.05, -0.4, -0.3, -0.2, 		 # right arm  
0, 0, -0.3490658, 0.6981317, -0.3490658, 0, 		 # left leg   
0, 0, -0.3490658, 0.6981317, -0.3490658, 0, 		 # right leg  
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 		 # left hand  
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, )		 # right hand 

inertiaRotor['romeo_hands_notoes'] = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
gearRatio['romeo_hands_notoes'] = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
