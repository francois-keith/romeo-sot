/*
 *  Copyright INRIA RHONES ALPES
 *
 *  Authors: Francois Keith
 *
 */

#ifndef ROMEONOTOES_H
#define ROMEONOTOES_H

/**
   \brief HALFSITTINGPOSITION  \

   chest       : 0
   head        : 0, 0, 0, 0
   left arm    : 86, 34, -29, -60, -23, -17, -11
   right arm   : 86, -34, 29, 60, -23, -17, -11
   left leg    : 0, 0, -29, 57, -29, 0
   right leg   : 0, 0, -29, 57, -29, 0
*/

#define HALFSITTINGPOSITION_DEG_OPENHRP {			\
   0		\
   0, 0, 0, 0		\
   86, 34, -29, -60, -23, -17, -11		\
   86, -34, 29, 60, -23, -17, -11		\
   0, 0, -29, 57, -29, 0		\
   0, 0, -29, 57, -29, 0

enum RomeoNoToesJointId {
  WAIST = 0,
  WAIST_TY,
  WAIST_TZ,
  WAIST_RX,
  WAIST_RY,
  WAIST_RZ,
  TrunkYaw_z,		// 6
  NeckYaw_z,		// 7
  NeckPitch_y,		// 8
  HeadPitch_y,		// 9
  HeadRoll_x,		// 10
  LShoulderPitch_y,		// 11
  LShoulderYaw_z,		// 12
  LElbowRoll_x,		// 13
  LElbowYaw_z,		// 14
  LWristRoll_x,		// 15
  LWristYaw_y,		// 16
  LWristPitch_z,		// 17
  RShoulderPitch_y,		// 18
  RShoulderYaw_z,		// 19
  RElbowRoll_x,		// 20
  RElbowYaw_z,		// 21
  RWristRoll_x,		// 22
  RWristYaw_y,		// 23
  RWristPitch_z,		// 24
  LHipYaw_z,		// 25
  LHipRoll_x,		// 26
  LHipPitch_y,		// 27
  LKneePitch_y,		// 28
  LAnklePitch_y,		// 29
  LAnkleRoll_x,		// 30
  RHipYaw_z,		// 31
  RHipRoll_x,		// 32
  RHipPitch_y,		// 33
  RKneePitch_y,		// 34
  RAnklePitch_y,		// 35
  RAnkleRoll_x,		// 36
};

#endif // ROMEONOTOES_H
