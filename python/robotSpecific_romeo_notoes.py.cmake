# --- ROBOT CONFIG -------------------------------------------------------------
from robotSpecific import pkgDataRootDir,modelName,robotDimension,initialConfig,gearRatio,inertiaRotor,specificitiesName,jointRankName

# RomeoNoToes data
pkgDataRootDir['romeo_notoes'] = "${CMAKE_INSTALL_PREFIX}/share/romeo"
modelName['romeo_notoes'] = 'RomeoNoToes.wrl'
specificitiesName['romeo_notoes'] = 'RomeoNoToesSpecificities.xml'
jointRankName['romeo_notoes'] = 'RomeoNoToesLinkJointRank.xml'
robotDimension['romeo_notoes'] = 37
initialConfig['romeo_notoes'] = (
0, 0, 0.840252, 0, 0, 0, 		 # FF 
0, 		 # chest      
0, 0, 0, 0, 		 # head       
1.5, 0.6, -0.5, -1.05, -0.4, -0.3, -0.2, 		 # left arm   
1.5, -0.6, 0.5, 1.05, -0.4, -0.3, -0.2, 		 # right arm  
0, 0, -0.3490658, 0.6981317, -0.3490658, 0, 		 # left leg   
0, 0, -0.3490658, 0.6981317, -0.3490658, 0, )		 # right leg  

inertiaRotor['romeo_notoes'] = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
gearRatio['romeo_notoes'] = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
