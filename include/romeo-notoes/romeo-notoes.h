/*
 *  Copyright JRL AIST-CNRS
 *
 *  Authors: Olivier Stasse (modif. 15/06/2010)
 *           Florent Lamiraux 
 * 
 */

#ifndef hrp2_10_small_H
#define hrp2_10_small_H

/**
   \brief HALFSITTINGPOSITION  \
 
   legs : 0.0, 0.0, -26.0, 50.0, -24.0, 0.0, 0.0, 0.0, -26.0, 50.0, -24.0, 0.0
 
   chest and head : 0.0, 0.0, 0.0, 0.0, 
 
   right arm : 15.0, -10.0, 0.0, -30.0, 0.0, 0.0, 0.0, 10.0, 
 
   left arm : 15.0,  10.0, 0.0, -30.0, 0.0, 0.0, 0.0, 10.0, 
 */

#define HALFSITTINGPOSITION_DEG_OPENHRP {						\
      0.0, 0.0, -26.0, 50.0, -24.0, 0.0, 0.0, 0.0, -26.0, 50.0, -24.0, 0.0, \
      0.0, 0.0, 0.0, 0.0,						\
	15.0, -10.0, 0.0, -30.0, 0.0, 0.0, 0.0, 10.0,			\
	15.0,  10.0, 0.0, -30.0, 0.0, 0.0, 0.0, 10.0,			\
      };

/**
   \brief HALFSITTINGPOSITION_RAD_KINEO  \
  
   FreeFlyer : 0.0, 0.0, 0.648702, 0.0 , 0.0, 0.0
 
   legs : 0.0, 0.0, -0.453785, 0.872664, -0.418879, 0.0, 0.0, 0.0, -0.453785, 0.872664, -0.48879, 0.0
 
   chest and head : 0.0, 0.0, 0.0, 0.0, 
 
   right arm : 0.261799, -0.174532, 0.0, -0.523598, 0.0, 0.0, 0.0, 0.174532, 

 
   left arm : 0.261799,  0.174532, 0.0, -0.523598, 0.0, 0.0, 0.0, 0.174532, 
 
*/
#define HALFSITTINGPOSITION_RAD_KINEO {					\
    0.0, 0.0, 0.648702, 0.0 , 0.0, 0.0,					\
      0.0, 0.0, -0.453785,0.872664,  -0.418879, 0.0, 0.0, 0.0, -0.453785,0.872664,  -0.418879, 0.0, \
      0.0, 0.0, 0.0, 0.0,						\
      0.261799, -0.174532, 0.0, -0.523598, 0.0, 0.0, 0.0, 0.174532,	\
      0.261799,  0.174532, 0.0,  -0.523598, 0.0, 0.0, 0.0, 0.174532,	\
      };


enum Hrp2JointId {
  WAIST = 0,
  WAIST_TY,
  WAIST_TZ,
  WAIST_RX,
  WAIST_RY,
  WAIST_RZ,
  RLEG_JOINT0,   // 6
  RLEG_JOINT1,   // 7
  RLEG_JOINT2,   // 8
  RLEG_JOINT3,   // 9
  RLEG_JOINT4,   // 10
  RLEG_JOINT5,   // 11
  LLEG_JOINT0,   // 12
  LLEG_JOINT1,   // 13
  LLEG_JOINT2,   // 14
  LLEG_JOINT3,   // 15
  LLEG_JOINT4,   // 16
  LLEG_JOINT5,   // 17
  CHEST_JOINT0,  // 18
  CHEST_JOINT1,  // 19
  HEAD_JOINT0,   // 20
  HEAD_JOINT1,   // 21
  RARM_JOINT0,   // 22
  RARM_JOINT1,   // 23
  RARM_JOINT2,   // 24
  RARM_JOINT3,   // 25
  RARM_JOINT4,   // 26
  RARM_JOINT5,   // 27
  RARM_JOINT6,   // 28
  RARM_JOINT7,   // 29
  LARM_JOINT0,   // 30
  LARM_JOINT1,   // 31
  LARM_JOINT2,   // 32
  LARM_JOINT3,   // 33
  LARM_JOINT4,   // 34
  LARM_JOINT5,   // 35
  LARM_JOINT6,   // 36
  LARM_JOINT7,   // 37
};

#endif
