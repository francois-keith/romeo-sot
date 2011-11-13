# --- ROBOT CONFIG -------------------------------------------------------------
from robotSpecific import pkgDataRootDir,modelName,robotDimension,initialConfig,gearRatio,inertiaRotor,specificitiesName,jointRankName

# Romeo data
modelName['romeo'] = 'Romeo.wrl'
specificitiesName['romeo'] = 'RomeoSpecificities.xml'
jointRankName['romeo'] = 'RomeoLinkJointRank.xml'
robotDimension['romeo'] = 39
initialConfig['romeo'] = (
0, 0, 0.840252, 0, 0, 0, 		 # FF 
0, 		 # chest      
0, 0, 0, 0, 		 # head       
1.5, 0.6, -0.5, -1.05, -0.4, -0.3, -0.2, 		 # left arm   
1.5, -0.6, 0.5, 1.05, -0.4, -0.3, -0.2, 		 # right arm  
0, 0, -0.3490658, 0.6981317, -0.3490658, 0, 0, 		 # left leg   
0, 0, -0.3490658, 0.6981317, -0.3490658, 0, 0, )		 # right leg  

inertiaRotor['romeo'] = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
gearRatio['romeo'] = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
