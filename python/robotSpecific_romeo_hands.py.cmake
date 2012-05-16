# --- ROBOT CONFIG -------------------------------------------------------------
from robotSpecific import pkgDataRootDir,modelName,robotDimension,initialConfig,gearRatio,inertiaRotor,specificitiesName,jointRankName

# RomeoHands data
pkgDataRootDir['romeo_hands'] = "${CMAKE_INSTALL_PREFIX}/share/romeo"
modelName['romeo_hands'] = 'RomeoHands.wrl'
specificitiesName['romeo_hands'] = 'RomeoHandsSpecificities.xml'
jointRankName['romeo_hands'] = 'RomeoHandsLinkJointRank.xml'
robotDimension['romeo_hands'] = 63
initialConfig['romeo_hands'] = (
0, 0, 0.840252, 0, 0, 0, 		 # FF 
0, 		 # chest      
0, 0, 0, 0, 		 # head       
1.5, 0.6, -0.5, -1.05, -0.4, -0.3, -0.2, 		 # left arm   
1.5, -0.6, 0.5, 1.05, -0.4, -0.3, -0.2, 		 # right arm  
0, 0, -0.3490658, 0.6981317, -0.3490658, 0, 0, 		 # left leg   
0, 0, -0.3490658, 0.6981317, -0.3490658, 0, 0, 		 # right leg  
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 		 # left hand   
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, )		 # right hand  

inertiaRotor['romeo_hands'] = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
gearRatio['romeo_hands'] = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
