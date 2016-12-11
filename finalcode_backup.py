# -*- encoding: UTF-8 -*- 

import math
# import almath as m # python's wrapping of almath
import sys
from naoqi import ALProxy
import time

def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

def StiffnessOff(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 0.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

def StandUp(proxy):
    proxy.goToPosture("StandInit", 1.0)

def SitDown(proxy):
    proxy.goToPosture("Sit", 1.0)

def Walk(proxy,x,y,theta):
    proxy.moveTo(x, y, theta)
    # self.onStopped()


def gesture_1_handwave(motionProxy) :

    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.68, 4.92])
    keys.append([0.00916195, 0.00916195])

    names.append("HeadYaw")
    times.append([0.68, 4.92])
    keys.append([-0.021518, -0.021518])

    names.append("LAnklePitch")
    times.append([0.68, 4.92])
    keys.append([-0.352862, -0.352862])

    names.append("LAnkleRoll")
    times.append([0.68, 4.92])
    keys.append([4.19617e-05, 4.19617e-05])

    names.append("LElbowRoll")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([-0.995524, -1.04921, -0.858998, -0.843658, -0.995524])

    names.append("LElbowYaw")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([-1.39905, -0.237812, -0.403484, -0.40962, -1.39905])

    names.append("LHand")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([0.2336, 0.6336, 0.6336, 0.6336, 0.2336])

    names.append("LHipPitch")
    times.append([0.68, 4.92])
    keys.append([-0.447886, -0.447886])

    names.append("LHipRoll")
    times.append([0.68, 4.92])
    keys.append([0.00310993, 0.00310993])

    names.append("LHipYawPitch")
    times.append([0.68, 4.92])
    keys.append([-0.00609398, -0.00609397])

    names.append("LKneePitch")
    times.append([0.68, 4.92])
    keys.append([0.699462, 0.699462])

    names.append("LShoulderPitch")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([1.41737, -0.935782, -1.00174, -0.891296, 1.41737])

    names.append("LShoulderRoll")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([0.28068, 0.354312, 1.04308, 0.36505, 0.28068])

    names.append("LWristYaw")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([-0.0614018, 0.31903, 0.31903, 0.31903, -0.0614019])

    names.append("RAnklePitch")
    times.append([0.68, 4.92])
    keys.append([-0.352778, -0.352778])

    names.append("RAnkleRoll")
    times.append([0.68, 4.92])
    keys.append([0.00157595, 0.00157595])

    names.append("RElbowRoll")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([0.997142, 1.0493, 1.0493, 1.0493, 0.997141])

    names.append("RElbowYaw")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([1.36215, 0.816046, 0.816046, 0.816046, 1.36215])

    names.append("RHand")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([0.246, 0.0408, 0.0408, 0.0408, 0.246])

    names.append("RHipPitch")
    times.append([0.68, 4.92])
    keys.append([-0.44797, -0.44797])

    names.append("RHipRoll")
    times.append([0.68, 4.92])
    keys.append([-0.00302601, -0.00302602])

    names.append("RHipYawPitch")
    times.append([0.68, 4.92])
    keys.append([-0.00609398, -0.00609397])

    names.append("RKneePitch")
    times.append([0.68, 4.92])
    keys.append([0.702614, 0.702614])

    names.append("RShoulderPitch")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([1.42666, 1.44047, 1.44047, 1.44047, 1.42666])

    names.append("RShoulderRoll")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([-0.265424, -0.154976, -0.154976, -0.154976, -0.265424])

    names.append("RWristYaw")
    times.append([0.68, 1.8, 2.76, 3.72, 4.92])
    keys.append([-0.016916, -0.11816, -0.11816, -0.11816, -0.016916])

    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

def gesture_2_attention(motionProxy):

    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.68])
    keys.append([0.00916195])

    names.append("HeadYaw")
    times.append([0.68])
    keys.append([-0.021518])

    names.append("LAnklePitch")
    times.append([0.68])
    keys.append([-0.352862])

    names.append("LAnkleRoll")
    times.append([0.68])
    keys.append([4.19617e-05])

    names.append("LElbowRoll")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([-0.995524, -0.0689881, -0.0349066, -1.08756])

    names.append("LElbowYaw")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([-1.39905, -0.326784, -0.971064, 0.53379])

    names.append("LHand")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([0.2336, 0.0148, 0.0184, 0.0184])

    names.append("LHipPitch")
    times.append([0.68])
    keys.append([-0.447886])

    names.append("LHipRoll")
    times.append([0.68])
    keys.append([0.00310993])

    names.append("LHipYawPitch")
    times.append([0.68])
    keys.append([-0.00609398])

    names.append("LKneePitch")
    times.append([0.68])
    keys.append([0.699462])

    names.append("LShoulderPitch")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([1.41737, 1.72571, 2.08567, 2.05245])

    names.append("LShoulderRoll")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([0.28068, 0.0137641, -0.239346, -0.131966])

    names.append("LWristYaw")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([-0.0614018, -1.56165, -0.771644, -1.55245])

    names.append("RAnklePitch")
    times.append([0.68])
    keys.append([-0.352778])

    names.append("RAnkleRoll")
    times.append([0.68])
    keys.append([0.00157595])

    names.append("RElbowRoll")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([0.997142, 0.181054, 0.046062, 1.08305])

    names.append("RElbowYaw")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([1.36215, 0.70253, 0.854396, -0.921976])

    names.append("RHand")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([0.246, 0.0700001, 0.0492001, 0.0704])

    names.append("RHipPitch")
    times.append([0.68])
    keys.append([-0.44797])

    names.append("RHipRoll")
    times.append([0.68])
    keys.append([-0.00302601])

    names.append("RHipYawPitch")
    times.append([0.68])
    keys.append([-0.00609398])

    names.append("RKneePitch")
    times.append([0.68])
    keys.append([0.702614])

    names.append("RShoulderPitch")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([1.42666, 1.68131, 2.06787, 1.93902])

    names.append("RShoulderRoll")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([-0.265424, -0.0798099, 0.176368, 0.0643861])

    names.append("RWristYaw")
    times.append([0.68, 2.08, 2.96, 6.8])
    keys.append([-0.016916, 0.92496, 0.515382, 0.834454])

    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err




    time.sleep(5)

    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([5.04])
    keys.append([0.00916195])

    names.append("HeadYaw")
    times.append([5.04])
    keys.append([-0.021518])

    names.append("LAnklePitch")
    times.append([5.04])
    keys.append([-0.352778])

    names.append("LAnkleRoll")
    times.append([5.04])
    keys.append([-0.00157595])

    names.append("LElbowRoll")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([-1.08756, -0.0349066, -0.0689881, -0.995524])

    names.append("LElbowYaw")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([0.53379, -0.971064, -0.326784, -1.39905])

    names.append("LHand")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([0.0184, 0.0184, 0.0148, 0.2336])

    names.append("LHipPitch")
    times.append([5.04])
    keys.append([-0.44797])

    names.append("LHipRoll")
    times.append([5.04])
    keys.append([0.00302601])

    names.append("LHipYawPitch")
    times.append([5.04])
    keys.append([-0.00609398])

    names.append("LKneePitch")
    times.append([5.04])
    keys.append([0.702614])

    names.append("LShoulderPitch")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([2.05245, 2.08567, 1.72571, 1.41737])

    names.append("LShoulderRoll")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([-0.131966, -0.239346, 0.0137641, 0.28068])

    names.append("LWristYaw")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([-1.55245, -0.771644, -1.56165, -0.0614018])

    names.append("RAnklePitch")
    times.append([5.04])
    keys.append([-0.352778])

    names.append("RAnkleRoll")
    times.append([5.04])
    keys.append([0.00157595])

    names.append("RElbowRoll")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([1.08756, 0.0349066, 0.0689881, 0.995524])

    names.append("RElbowYaw")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([-0.53379, 0.971064, 0.326784, 1.39905])

    names.append("RHand")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([0.0184, 0.0184, 0.0148, 0.2336])

    names.append("RHipPitch")
    times.append([5.04])
    keys.append([-0.44797])

    names.append("RHipRoll")
    times.append([5.04])
    keys.append([-0.00302601])

    names.append("RHipYawPitch")
    times.append([5.04])
    keys.append([-0.00609398])

    names.append("RKneePitch")
    times.append([5.04])
    keys.append([0.702614])

    names.append("RShoulderPitch")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([2.05245, 2.08567, 1.72571, 1.41737])

    names.append("RShoulderRoll")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([0.131966, 0.239346, -0.0137641, -0.28068])

    names.append("RWristYaw")
    times.append([1.6, 3.2, 4.08, 5.04])
    keys.append([1.55245, 0.771644, 1.56165, 0.0614018])

    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err


    time.sleep(3)

    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.12, 3.4])
    keys.append([0.25, 0.00916195])

    names.append("HeadYaw")
    times.append([1.12, 3.4])
    keys.append([-0.092082, -0.021518])

    names.append("LAnklePitch")
    times.append([1.12, 3.4])
    keys.append([-1.16281, -0.352778])

    names.append("LAnkleRoll")
    times.append([1.12, 3.4])
    keys.append([0.0061779, -0.00157595])

    names.append("LElbowRoll")
    times.append([1.12, 3.4])
    keys.append([-1.54163, -0.995524])

    names.append("LElbowYaw")
    times.append([1.12, 3.4])
    keys.append([-0.62438, -1.39905])

    names.append("LHand")
    times.append([1.12, 3.4])
    keys.append([0.4936, 0.2336])

    names.append("LHipPitch")
    times.append([1.12, 3.4])
    keys.append([-0.811444, -0.44797])

    names.append("LHipRoll")
    times.append([1.12, 3.4])
    keys.append([0.314512, 0.00302601])

    names.append("LHipYawPitch")
    times.append([1.12, 3.4])
    keys.append([-0.18097, -0.00609398])

    names.append("LKneePitch")
    times.append([1.12, 3.4])
    keys.append([2.10921, 0.702614])

    names.append("LShoulderPitch")
    times.append([1.12, 3.4])
    keys.append([0.674918, 1.41737])

    names.append("LShoulderRoll")
    times.append([1.12, 3.4])
    keys.append([-0.291502, 0.28068])

    names.append("LWristYaw")
    times.append([1.12, 3.4])
    keys.append([-1.11526, -0.0614018])

    names.append("RAnklePitch")
    times.append([1.12, 3.4])
    keys.append([-1.15506, -0.352778])

    names.append("RAnkleRoll")
    times.append([1.12, 3.4])
    keys.append([0.0123138, 0.00157595])

    names.append("RElbowRoll")
    times.append([1.12, 3.4])
    keys.append([0.905102, 0.995524])

    names.append("RElbowYaw")
    times.append([1.12, 3.4])
    keys.append([0.766958, 1.39905])

    names.append("RHand")
    times.append([1.12, 3.4])
    keys.append([0.0516, 0.2336])

    names.append("RHipPitch")
    times.append([1.12, 3.4])
    keys.append([-0.282298, -0.44797])

    names.append("RHipRoll")
    times.append([1.12, 3.4])
    keys.append([0.342124, -0.00302601])

    names.append("RHipYawPitch")
    times.append([1.12, 3.4])
    keys.append([-0.18097, -0.00609398])

    names.append("RKneePitch")
    times.append([1.12, 3.4])
    keys.append([1.62148, 0.702614])

    names.append("RShoulderPitch")
    times.append([1.12, 3.4])
    keys.append([1.50796, 1.41737])

    names.append("RShoulderRoll")
    times.append([1.12, 3.4])
    keys.append([0.167164, -0.28068])

    names.append("RWristYaw")
    times.append([1.12, 3.4])
    keys.append([-0.139636, 0.0614018])

    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print err

def gesture_3_leaning(motionProxy):
    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1])
    keys.append([0.0843279])

    names.append("HeadYaw")
    times.append([1])
    keys.append([0.0106959])

    names.append("LAnklePitch")
    times.append([1])
    keys.append([-0.527738])

    names.append("LAnkleRoll")
    times.append([1])
    keys.append([-0.300622])

    names.append("LElbowRoll")
    times.append([1])
    keys.append([-0.469362])

    names.append("LElbowYaw")
    times.append([1])
    keys.append([-0.926578])

    names.append("LHand")
    times.append([1])
    keys.append([0.0256])

    names.append("LHipPitch")
    times.append([1])
    keys.append([-0.207048])

    names.append("LHipRoll")
    times.append([1])
    keys.append([0.527738])

    names.append("LHipYawPitch")
    times.append([1])
    keys.append([-0.374254])

    names.append("LKneePitch")
    times.append([1])
    keys.append([0.918824])

    names.append("LShoulderPitch")
    times.append([1])
    keys.append([1.36215])

    names.append("LShoulderRoll")
    times.append([1])
    keys.append([-0.196394])

    names.append("LWristYaw")
    times.append([1])
    keys.append([0.470896])

    names.append("RAnklePitch")
    times.append([1])
    keys.append([-0.220854])

    names.append("RAnkleRoll")
    times.append([1])
    keys.append([0.191792])

    names.append("RElbowRoll")
    times.append([1])
    keys.append([0.1335])

    names.append("RElbowYaw")
    times.append([1])
    keys.append([0.793036])

    names.append("RHand")
    times.append([1])
    keys.append([0.348])

    names.append("RHipPitch")
    times.append([1])
    keys.append([0.11961])

    names.append("RHipRoll")
    times.append([1])
    keys.append([0.0782759])

    names.append("RHipYawPitch")
    times.append([1])
    keys.append([-0.374254])

    names.append("RKneePitch")
    times.append([1])
    keys.append([0.397348])

    names.append("RShoulderPitch")
    times.append([1])
    keys.append([1.24565])

    names.append("RShoulderRoll")
    times.append([1])
    keys.append([0.314159])

    names.append("RWristYaw")
    times.append([1])
    keys.append([0.639636])


    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

def gesture_4_shrugging(motionProxy):
    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.12])
    keys.append([-0.01845])

    names.append("HeadYaw")
    times.append([1.12])
    keys.append([-0.0337899])

    names.append("LAnklePitch")
    times.append([1.12])
    keys.append([-0.352862])

    names.append("LAnkleRoll")
    times.append([1.12])
    keys.append([-0.00149202])

    names.append("LElbowRoll")
    times.append([1.12])
    keys.append([-1.49101])

    names.append("LElbowYaw")
    times.append([1.12])
    keys.append([-2.08567])

    names.append("LHand")
    times.append([1.12])
    keys.append([0.2536])

    names.append("LHipPitch")
    times.append([1.12])
    keys.append([-0.444818])

    names.append("LHipRoll")
    times.append([1.12])
    keys.append([-0.00149202])

    names.append("LHipYawPitch")
    times.append([1.12])
    keys.append([0.00157595])

    names.append("LKneePitch")
    times.append([1.12])
    keys.append([0.693326])

    names.append("LShoulderPitch")
    times.append([1.12])
    keys.append([0.0597839])

    names.append("LShoulderRoll")
    times.append([1.12])
    keys.append([0.240796])

    names.append("LWristYaw")
    times.append([1.12])
    keys.append([-0.216336])

    names.append("RAnklePitch")
    times.append([1.12])
    keys.append([-0.34971])

    names.append("RAnkleRoll")
    times.append([1.12])
    keys.append([-0.00149202])

    names.append("RElbowRoll")
    times.append([1.12])
    keys.append([1.51103])

    names.append("RElbowYaw")
    times.append([1.12])
    keys.append([2.08567])

    names.append("RHand")
    times.append([1.12])
    keys.append([0.158])

    names.append("RHipPitch")
    times.append([1.12])
    keys.append([-0.44797])

    names.append("RHipRoll")
    times.append([1.12])
    keys.append([0.0061779])

    names.append("RHipYawPitch")
    times.append([1.12])
    keys.append([0.00157595])

    names.append("RKneePitch")
    times.append([1.12])
    keys.append([0.696478])

    names.append("RShoulderPitch")
    times.append([1.12])
    keys.append([0.0337899])

    names.append("RShoulderRoll")
    times.append([1.12])
    keys.append([-0.016916])

    names.append("RWristYaw")
    times.append([1.12])
    keys.append([-0.096684])

    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

def gesture_5_arms(motionProxy):

    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.6, 7.6])
    keys.append([0.00916195, 0.00916195])

    names.append("HeadYaw")
    times.append([1.6, 7.6])
    keys.append([-0.021518, -0.021518])

    names.append("LAnklePitch")
    times.append([1.6, 7.6])
    keys.append([-0.352778, -0.352778])

    names.append("LAnkleRoll")
    times.append([1.6, 7.6])
    keys.append([-0.00157595, -0.00157595])

    names.append("LElbowRoll")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([-0.995524, -0.662646, -0.421808, -0.662646, -0.421808, -0.995524])

    names.append("LElbowYaw")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([-1.39905, -1.08305, -1.08305, -1.08305, -1.08305, -1.39905])

    names.append("LHand")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([0.2336, 0.6844, 0.6844, 0.6844, 0.6844, 0.2336])

    names.append("LHipPitch")
    times.append([1.6, 7.6])
    keys.append([-0.44797, -0.44797])

    names.append("LHipRoll")
    times.append([1.6, 7.6])
    keys.append([0.00302601, 0.00302602])

    names.append("LHipYawPitch")
    times.append([1.6, 7.6])
    keys.append([-0.00609398, -0.00609397])

    names.append("LKneePitch")
    times.append([1.6, 7.6])
    keys.append([0.702614, 0.702614])

    names.append("LShoulderPitch")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([1.41737, 0.294486, 1.65668, 0.294486, 1.65668, 1.41737])

    names.append("LShoulderRoll")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([0.28068, 0.371186, 0.262272, 0.371186, 0.262272, 0.28068])

    names.append("LWristYaw")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([-0.0614018, 0.83292, 0.866668, 0.83292, 0.866668, -0.0614019])

    names.append("RAnklePitch")
    times.append([1.6, 7.6])
    keys.append([-0.352778, -0.352778])

    names.append("RAnkleRoll")
    times.append([1.6, 7.6])
    keys.append([0.00157595, 0.00157595])

    names.append("RElbowRoll")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([0.995524, 0.587564, 0.121228, 0.587563, 0.121228, 0.995524])

    names.append("RElbowYaw")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([1.39905, 1.05995, 1.05995, 1.05995, 1.05995, 1.39905])

    names.append("RHand")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([0.2336, 0.7204, 0.7204, 0.7204, 0.7204, 0.2336])

    names.append("RHipPitch")
    times.append([1.6, 7.6])
    keys.append([-0.44797, -0.44797])

    names.append("RHipRoll")
    times.append([1.6, 7.6])
    keys.append([-0.00302601, -0.00302602])

    names.append("RHipYawPitch")
    times.append([1.6, 7.6])
    keys.append([-0.00609398, -0.00609397])

    names.append("RKneePitch")
    times.append([1.6, 7.6])
    keys.append([0.702614, 0.702614])

    names.append("RShoulderPitch")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([1.41737, 0.184122, 1.29934, 0.184122, 1.29934, 1.41737])

    names.append("RShoulderRoll")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([-0.28068, -0.220938, -0.184122, -0.220938, -0.184122, -0.28068])

    names.append("RWristYaw")
    times.append([1.6, 2.8, 4, 5.2, 6.4, 7.6])
    keys.append([0.0614018, -1.02015, -1.05237, -1.02015, -1.05237, 0.0614019])

    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

def gesture_6_bored(motionProxy):
    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.12, 3.36])
    keys.append([0.00916195, 0.25])

    names.append("HeadYaw")
    times.append([1.12, 3.36])
    keys.append([-0.021518, -0.092082])

    names.append("LAnklePitch")
    times.append([1.12, 3.36])
    keys.append([-0.352778, -1.16281])

    names.append("LAnkleRoll")
    times.append([1.12, 3.36])
    keys.append([-0.00157595, 0.0061779])

    names.append("LElbowRoll")
    times.append([1.12, 3.36])
    keys.append([-0.995524, -1.54163])

    names.append("LElbowYaw")
    times.append([1.12, 3.36])
    keys.append([-1.39905, -0.62438])

    names.append("LHand")
    times.append([1.12, 3.36])
    keys.append([0.2336, 0.4936])

    names.append("LHipPitch")
    times.append([1.12, 3.36])
    keys.append([-0.44797, -0.811444])

    names.append("LHipRoll")
    times.append([1.12, 3.36])
    keys.append([0.00302601, 0.314512])

    names.append("LHipYawPitch")
    times.append([1.12, 3.36])
    keys.append([-0.00609398, -0.18097])

    names.append("LKneePitch")
    times.append([1.12, 3.36])
    keys.append([0.702614, 2.10921])

    names.append("LShoulderPitch")
    times.append([1.12, 3.36])
    keys.append([1.41737, 0.674918])

    names.append("LShoulderRoll")
    times.append([1.12, 3.36])
    keys.append([0.28068, -0.291502])

    names.append("LWristYaw")
    times.append([1.12, 3.36])
    keys.append([-0.0614018, -1.11526])

    names.append("RAnklePitch")
    times.append([1.12, 3.36])
    keys.append([-0.352778, -1.15506])

    names.append("RAnkleRoll")
    times.append([1.12, 3.36])
    keys.append([0.00157595, 0.0123138])

    names.append("RElbowRoll")
    times.append([1.12, 3.36])
    keys.append([0.995524, 0.905102])

    names.append("RElbowYaw")
    times.append([1.12, 3.36])
    keys.append([1.39905, 0.766958])

    names.append("RHand")
    times.append([1.12, 3.36])
    keys.append([0.2336, 0.0516])

    names.append("RHipPitch")
    times.append([1.12, 3.36])
    keys.append([-0.44797, -0.282298])

    names.append("RHipRoll")
    times.append([1.12, 3.36])
    keys.append([-0.00302601, 0.342124])

    names.append("RHipYawPitch")
    times.append([1.12, 3.36])
    keys.append([-0.00609398, -0.18097])

    names.append("RKneePitch")
    times.append([1.12, 3.36])
    keys.append([0.702614, 1.62148])

    names.append("RShoulderPitch")
    times.append([1.12, 3.36])
    keys.append([1.41737, 1.50796])

    names.append("RShoulderRoll")
    times.append([1.12, 3.36])
    keys.append([-0.28068, 0.167164])

    names.append("RWristYaw")
    times.append([1.12, 3.36])
    keys.append([0.0614018, -0.139636])

    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

def gesture_7_coverears(motionProxy):
    # Choregraphe simplified export in Python.

    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.6, 3.76])
    keys.append([0.00916195, 0.508257])

    names.append("HeadYaw")
    times.append([1.6, 3.76])
    keys.append([-0.021518, -0.0644701])

    names.append("LAnklePitch")
    times.append([1.6])
    keys.append([-0.352778])

    names.append("LAnkleRoll")
    times.append([1.6])
    keys.append([-0.00157595])

    names.append("LElbowRoll")
    times.append([1.6, 3.76])
    keys.append([-0.995524, -1.53242])

    names.append("LElbowYaw")
    times.append([1.6, 3.76])
    keys.append([-1.39905, -1.37757])

    names.append("LHand")
    times.append([1.6, 3.76])
    keys.append([0.2336, 0.022])

    names.append("LHipPitch")
    times.append([1.6])
    keys.append([-0.44797])

    names.append("LHipRoll")
    times.append([1.6])
    keys.append([0.00302601])

    names.append("LHipYawPitch")
    times.append([1.6])
    keys.append([-0.00609398])

    names.append("LKneePitch")
    times.append([1.6])
    keys.append([0.702614])

    names.append("LShoulderPitch")
    times.append([1.6, 3.76])
    keys.append([1.41737, -0.733294])

    names.append("LShoulderRoll")
    times.append([1.6, 3.76])
    keys.append([0.28068, -0.173384])

    names.append("LWristYaw")
    times.append([1.6, 3.76])
    keys.append([-0.0614018, -0.00924587])

    names.append("RAnklePitch")
    times.append([1.6])
    keys.append([-0.352778])

    names.append("RAnkleRoll")
    times.append([1.6])
    keys.append([0.00157595])

    names.append("RElbowRoll")
    times.append([1.6, 3.76])
    keys.append([0.995524, 1.53251])

    names.append("RElbowYaw")
    times.append([1.6, 3.76])
    keys.append([1.39905, 1.34221])

    names.append("RHand")
    times.append([1.6, 3.76])
    keys.append([0.2336, 0.0412])

    names.append("RHipPitch")
    times.append([1.6])
    keys.append([-0.44797])

    names.append("RHipRoll")
    times.append([1.6])
    keys.append([-0.00302601])

    names.append("RHipYawPitch")
    times.append([1.6])
    keys.append([-0.00609398])

    names.append("RKneePitch")
    times.append([1.6])
    keys.append([0.702614])

    names.append("RShoulderPitch")
    times.append([1.6, 3.76])
    keys.append([1.41737, -0.728608])

    names.append("RShoulderRoll")
    times.append([1.6, 3.76])
    keys.append([-0.28068, 0.130348])

    names.append("RWristYaw")
    times.append([1.6, 3.76])
    keys.append([0.0614018, 0.51078])

    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

def gesture_8_tilt_head(motionProxy):
    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.16, 2.24])
    keys.append([0.00916195, 0.325166])

    names.append("HeadYaw")
    times.append([1.16, 2.24])
    keys.append([-0.021518, -0.895898])

    names.append("LAnklePitch")
    times.append([1.16])
    keys.append([-0.352778])

    names.append("LAnkleRoll")
    times.append([1.16])
    keys.append([-0.00157595])

    names.append("LElbowRoll")
    times.append([1.16, 2.24])
    keys.append([-0.995524, -1.54462])

    names.append("LElbowYaw")
    times.append([1.16, 2.24])
    keys.append([-1.39905, -1.13213])

    names.append("LHand")
    times.append([1.16, 2.24])
    keys.append([0.2336, 0.6428])

    names.append("LHipPitch")
    times.append([1.16])
    keys.append([-0.44797])

    names.append("LHipRoll")
    times.append([1.16])
    keys.append([0.00302601])

    names.append("LHipYawPitch")
    times.append([1.16])
    keys.append([-0.00609398])

    names.append("LKneePitch")
    times.append([1.16])
    keys.append([0.702614])

    names.append("LShoulderPitch")
    times.append([1.16, 2.24])
    keys.append([1.41737, 0.217786])

    names.append("LShoulderRoll")
    times.append([1.16, 2.24])
    keys.append([0.28068, -0.18719])

    names.append("LWristYaw")
    times.append([1.16, 2.24])
    keys.append([-0.0614018, -0.216336])

    names.append("RAnklePitch")
    times.append([1.16])
    keys.append([-0.352778])

    names.append("RAnkleRoll")
    times.append([1.16])
    keys.append([0.00157595])

    names.append("RElbowRoll")
    times.append([1.16, 2.24])
    keys.append([0.995524, 0.998676])

    names.append("RElbowYaw")
    times.append([1.16, 2.24])
    keys.append([1.39905, 0.808376])

    names.append("RHand")
    times.append([1.16, 2.24])
    keys.append([0.2336, 0.0436])

    names.append("RHipPitch")
    times.append([1.16])
    keys.append([-0.44797])

    names.append("RHipRoll")
    times.append([1.16])
    keys.append([-0.00302601])

    names.append("RHipYawPitch")
    times.append([1.16])
    keys.append([-0.00609398])

    names.append("RKneePitch")
    times.append([1.16])
    keys.append([0.702614])

    names.append("RShoulderPitch")
    times.append([1.16, 2.24])
    keys.append([1.41737, 1.43126])

    names.append("RShoulderRoll")
    times.append([1.16, 2.24])
    keys.append([-0.28068, -0.159578])

    names.append("RWristYaw")
    times.append([1.16, 2.24])
    keys.append([0.0614018, -0.108956])


    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err


    time.sleep(2)


    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.08, 2.28])
    keys.append([0.325166, 0.00916195])

    names.append("HeadYaw")
    times.append([1.08, 2.28])
    keys.append([-0.895898, -0.021518])

    names.append("LAnklePitch")
    times.append([2.28])
    keys.append([-0.352778])

    names.append("LAnkleRoll")
    times.append([2.28])
    keys.append([-0.00157595])

    names.append("LElbowRoll")
    times.append([1.08, 2.28])
    keys.append([-1.54462, -0.995524])

    names.append("LElbowYaw")
    times.append([1.08, 2.28])
    keys.append([-1.13213, -1.39905])

    names.append("LHand")
    times.append([1.08, 2.28])
    keys.append([0.6428, 0.2336])

    names.append("LHipPitch")
    times.append([2.28])
    keys.append([-0.44797])

    names.append("LHipRoll")
    times.append([2.28])
    keys.append([0.00302601])

    names.append("LHipYawPitch")
    times.append([2.28])
    keys.append([-0.00609398])

    names.append("LKneePitch")
    times.append([2.28])
    keys.append([0.702614])

    names.append("LShoulderPitch")
    times.append([1.08, 2.28])
    keys.append([0.217786, 1.41737])

    names.append("LShoulderRoll")
    times.append([1.08, 2.28])
    keys.append([-0.18719, 0.28068])

    names.append("LWristYaw")
    times.append([1.08, 2.28])
    keys.append([-0.216336, -0.0614018])

    names.append("RAnklePitch")
    times.append([2.28])
    keys.append([-0.352778])

    names.append("RAnkleRoll")
    times.append([2.28])
    keys.append([0.00157595])

    names.append("RElbowRoll")
    times.append([1.08, 2.28])
    keys.append([0.998676, 0.995524])

    names.append("RElbowYaw")
    times.append([1.08, 2.28])
    keys.append([0.808376, 1.39905])

    names.append("RHand")
    times.append([1.08, 2.28])
    keys.append([0.0436, 0.2336])

    names.append("RHipPitch")
    times.append([2.28])
    keys.append([-0.44797])

    names.append("RHipRoll")
    times.append([2.28])
    keys.append([-0.00302601])

    names.append("RHipYawPitch")
    times.append([2.28])
    keys.append([-0.00609398])

    names.append("RKneePitch")
    times.append([2.28])
    keys.append([0.702614])

    names.append("RShoulderPitch")
    times.append([1.08, 2.28])
    keys.append([1.43126, 1.41737])

    names.append("RShoulderRoll")
    times.append([1.08, 2.28])
    keys.append([-0.159578, -0.28068])

    names.append("RWristYaw")
    times.append([1.08, 2.28])
    keys.append([-0.108956, 0.0614018])


    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

def gesture_9_nod(motionProxy):

    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()
    names.append("HeadPitch")
    times.append([1.16, 2.52, 3.84, 5.12, 6.44])
    keys.append([0.024502, 0.511469, 0.024502, 0.511469, 0.024502])

    names.append("HeadYaw")
    times.append([1.16, 2.52, 3.84, 5.12, 6.44])
    keys.append([-0.024586, -0.024586, -0.0245859, -0.0245859, -0.0245859])

    names.append("LAnklePitch")
    times.append([1.16, 3.84, 6.44])
    keys.append([-0.352862, -0.352862, -0.352862])

    names.append("LAnkleRoll")
    times.append([1.16, 3.84, 6.44])
    keys.append([-0.00609398, -0.00609397, -0.00609397])

    names.append("LElbowRoll")
    times.append([1.16, 3.84, 6.44])
    keys.append([-0.998592, -0.998592, -0.998592])

    names.append("LElbowYaw")
    times.append([1.16, 3.84, 6.44])
    keys.append([-1.35763, -1.35763, -1.35763])

    names.append("LHand")
    times.append([1.16, 3.84, 6.44])
    keys.append([0.2612, 0.2612, 0.2612])

    names.append("LHipPitch")
    times.append([1.16, 3.84, 6.44])
    keys.append([-0.450954, -0.450955, -0.450955])

    names.append("LHipRoll")
    times.append([1.16, 3.84, 6.44])
    keys.append([0.00157595, 0.00157595, 0.00157595])

    names.append("LHipYawPitch")
    times.append([1.16, 3.84, 6.44])
    keys.append([4.19617e-05, 4.19617e-05, 4.19617e-05])

    names.append("LKneePitch")
    times.append([1.16, 3.84, 6.44])
    keys.append([0.707132, 0.707132, 0.707132])

    names.append("LShoulderPitch")
    times.append([1.16, 3.84, 6.44])
    keys.append([1.40357, 1.40357, 1.40357])

    names.append("LShoulderRoll")
    times.append([1.16, 3.84, 6.44])
    keys.append([0.262272, 0.262272, 0.262272])

    names.append("LWristYaw")
    times.append([1.16, 3.84, 6.44])
    keys.append([-0.023052, -0.023052, -0.023052])

    names.append("RAnklePitch")
    times.append([1.16, 3.84, 6.44])
    keys.append([-0.346642, -0.346642, -0.346642])

    names.append("RAnkleRoll")
    times.append([1.16, 3.84, 6.44])
    keys.append([4.19617e-05, 4.19617e-05, 4.19617e-05])

    names.append("RElbowRoll")
    times.append([1.16, 3.84, 6.44])
    keys.append([0.975666, 0.975665, 0.975665])

    names.append("RElbowYaw")
    times.append([1.16, 3.84, 6.44])
    keys.append([1.36675, 1.36675, 1.36675])

    names.append("RHand")
    times.append([1.16, 3.84, 6.44])
    keys.append([0.244, 0.244, 0.244])

    names.append("RHipPitch")
    times.append([1.16, 3.84, 6.44])
    keys.append([-0.454106, -0.454105, -0.454105])

    names.append("RHipRoll")
    times.append([1.16, 3.84, 6.44])
    keys.append([0.0061779, 0.00617791, 0.00617791])

    names.append("RHipYawPitch")
    times.append([1.16, 3.84, 6.44])
    keys.append([4.19617e-05, 4.19617e-05, 4.19617e-05])

    names.append("RKneePitch")
    times.append([1.16, 3.84, 6.44])
    keys.append([0.699546, 0.699545, 0.699545])

    names.append("RShoulderPitch")
    times.append([1.16, 3.84, 6.44])
    keys.append([1.4328, 1.4328, 1.4328])

    names.append("RShoulderRoll")
    times.append([1.16, 3.84, 6.44])
    keys.append([-0.270026, -0.270025, -0.270025])

    names.append("RWristYaw")
    times.append([1.16, 3.84, 6.44])
    keys.append([-0.0123138, -0.0123138, -0.0123138])


    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

def gesture_confused(motionProxy):

    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.429478, 0.420274, 0.479767, 0.332836])

    names.append("HeadYaw")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-0.354396, -0.47865, -0.193326, 0.50311])

    names.append("LAnklePitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-0.34826, -0.34826, -0.352862, -0.349794])

    names.append("LAnkleRoll")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.00771189, 0.00771189, 0.00771189, 0.00771189])

    names.append("LElbowRoll")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-1.00166, -0.990922, -0.990922, -0.990922])

    names.append("LElbowYaw")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-1.35456, -1.38678, -1.38678, -1.38678])

    names.append("LHand")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.4112, 0.4112, 0.4112, 0.4112])

    names.append("LHipPitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-0.44942, -0.44942, -0.44942, -0.450954])

    names.append("LHipRoll")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-0.00302601, -0.00302601, -0.00302601, -0.00302601])

    names.append("LHipYawPitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.00157595, -0.00762796, 0.00310993, 0.00310993])

    names.append("LKneePitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.69486, 0.704064, 0.696394, 0.704064])

    names.append("LShoulderPitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([1.54163, 1.52782, 1.52782, 1.52782])

    names.append("LShoulderRoll")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.0858622, 0.098134, 0.098134, 0.0873961])

    names.append("LWristYaw")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.0168321, -0.01845, -0.01845, -0.01845])

    names.append("RAnklePitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-0.360448, -0.360448, -0.360448, -0.34971])

    names.append("RAnkleRoll")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-0.00609398, -0.00609398, -0.00609398, -0.00609398])

    names.append("RElbowRoll")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([1.12907, 1.16895, 1.15821, 1.15208])

    names.append("RElbowYaw")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.952572, 0.820648, 0.95564, 0.943368])

    names.append("RHand")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.0391999, 0.0391999, 0.0391999, 0.0391999])

    names.append("RHipPitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-0.44797, -0.472514, -0.451038, -0.444902])

    names.append("RHipRoll")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.00157595, 0.00157595, 0.00157595, 0.00157595])

    names.append("RHipYawPitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.00157595, -0.00762796, 0.00310993, 0.00310993])

    names.append("RKneePitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.704148, 0.702614, 0.698012, 0.690342])

    names.append("RShoulderPitch")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-0.724006, -0.279146, -0.77923, -0.776162])

    names.append("RShoulderRoll")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([-0.328318, -0.277696, -0.323716, -0.319114])

    names.append("RWristYaw")
    times.append([0.64, 1.28, 1.84, 2.48])
    keys.append([0.314428, 0.30369, 0.30369, 0.297554])

    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

def squat(motionProxy):

    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.6])
    keys.append([0.0674541])

    names.append("HeadYaw")
    times.append([0.6])
    keys.append([-0.0276539])

    names.append("LAnklePitch")
    times.append([0.6])
    keys.append([-1.18276])

    names.append("LAnkleRoll")
    times.append([0.6])
    keys.append([0.070606])

    names.append("LElbowRoll")
    times.append([0.6])
    keys.append([-1.03848])

    names.append("LElbowYaw")
    times.append([0.6])
    keys.append([-0.794654])

    names.append("LHand")
    times.append([0.6])
    keys.append([0.0192])

    names.append("LHipPitch")
    times.append([0.6])
    keys.append([-0.700996])

    names.append("LHipRoll")
    times.append([0.6])
    keys.append([-0.076658])

    names.append("LHipYawPitch")
    times.append([0.6])
    keys.append([-0.237728])

    names.append("LKneePitch")
    times.append([0.6])
    keys.append([2.10767])

    names.append("LShoulderPitch")
    times.append([0.6])
    keys.append([1.44959])

    names.append("LShoulderRoll")
    times.append([0.6])
    keys.append([0.0873961])

    names.append("LWristYaw")
    times.append([0.6])
    keys.append([0.0843279])

    names.append("RAnklePitch")
    times.append([0.6])
    keys.append([-1.1863])

    names.append("RAnkleRoll")
    times.append([0.6])
    keys.append([-0.078192])

    names.append("RElbowRoll")
    times.append([0.6])
    keys.append([1.02782])

    names.append("RElbowYaw")
    times.append([0.6])
    keys.append([0.823716])

    names.append("RHand")
    times.append([0.6])
    keys.append([0.0172])

    names.append("RHipPitch")
    times.append([0.6])
    keys.append([-0.698012])

    names.append("RHipRoll")
    times.append([0.6])
    keys.append([0.07214])

    names.append("RHipYawPitch")
    times.append([0.6])
    keys.append([-0.237728])

    names.append("RKneePitch")
    times.append([0.6])
    keys.append([2.10622])

    names.append("RShoulderPitch")
    times.append([0.6])
    keys.append([1.44967])

    names.append("RShoulderRoll")
    times.append([0.6])
    keys.append([-0.0844119])

    names.append("RWristYaw")
    times.append([0.6])
    keys.append([-0.0583339])


    try:
      motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
      print err

def begin_presentation():
    start = False
    syncFile = open('output/sync.txt', 'r')
    while not start:
        # read sync
        where = syncFile.tell()
        line = syncFile.readline()
        if not line or line in ['\n', '\r\n']:
            time.sleep(1)
            syncFile.seek(where)
        else:
            if line.rstrip('\n') == "start":
                start = True
    print "Sync File has announced start"

def end_presentation():
    start = False
    syncFile = open('output/sync.txt', 'r')
    while not start:
        # read sync
        where = syncFile.tell()
        line = syncFile.readline()
        if not line or line in ['\n', '\r\n']:
            time.sleep(1)
            syncFile.seek(where)
        else:
            if line.rstrip('\n') == "end":
                start = True
    print "Sync File has announced end"

def decode_input(char,motionProxy):
    if char == 1:
        gesture_1_handwave(motionProxy)

    elif char == 2:
        gesture_2_attention(motionProxy)

    elif char == 3:
        gesture_3_leaning(motionProxy)

    elif char == 4:
        gesture_4_shrugging(motionProxy)

    elif char ==5:
        gesture_5_arms(motionProxy)

    elif char ==6:
        gesture_6_bored(motionProxy)

    elif char ==7:
        gesture_7_coverears(motionProxy)

    elif char ==8:
        gesture_8_tilt_head(motionProxy)

    else:
        gesture_9_nod(motionProxy)
 
def main(robotIP,robotPort):

    # kinetic_feedbackfile = open('../output/kinetic_feedback.txt', 'w')
    # kinetic_feedbackfile.close()


    #==================initialise the NAO===========================
    print "Initialising NAO"
    #Setting the Proxies
    try:
        motionProxy = ALProxy("ALMotion", robotIP, robotPort)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e

    try:
        ttsProxy = ALProxy("ALTextToSpeech", robotIP, robotPort)
    except Exception, e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ", e

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, robotPort)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e


    try:
        animatedSpeechProxy = ALProxy("ALAnimatedSpeech", robotIP, robotPort)    
    except Exception, e:
        print "Could not create proxy to ALAnimatedSpeech"
        print "Error was: ", e

    # Turn on the Motors
    motionProxy.wakeUp()

    # say the text with the local configuration
    # animatedSpeechProxy.say("Guess who's back, back again", gesture_confused)

    #StandUp
    StandUp(postureProxy)
    # motionProxy.rest()

    gesture_1_handwave(motionProxy)
    print "handwave gesture"

    time.sleep(1)

    gesture_2_attention(motionProxy)
    print "attention"

    time.sleep(1)


    gesture_3_leaning(motionProxy)
    print "leaning"

    time.sleep(1)


    gesture_4_shrugging(motionProxy)
    print "shrugging"

    time.sleep(1)


    gesture_5_arms(motionProxy)
    print "raise up and down"

    time.sleep(1)


    gesture_6_bored(motionProxy)
    print "Bored"                    

    time.sleep(1)


    gesture_7_coverears(motionProxy)
    print "Cover ears"                    

    time.sleep(1)


    gesture_8_tilt_head(motionProxy)
    print "tilt head"                    

    gesture_9_nod(motionProxy)
    print "Nodding Head and standing chill" 


    #==================Check for Presentation to Begin===========================

    start = False
    syncFile = open('../output/sync.txt', 'r')
    while not start:
        # read sync
        where = syncFile.tell()
        line = syncFile.readline()
        if not line or line in ['\n', '\r\n']:
            time.sleep(1)
            syncFile.seek(where)
        else:
            if line.rstrip('\n') == "start":
                start = True
    print "Sync File has announced start"
    print "Begin Presentation"


    # Turn on the Motors
    motionProxy.wakeUp()
    animatedSpeechProxy.say("Begin Presentation", gesture_confused)



    #================== Detecting inputs ===========================

    # #Listening State
    # gesture_9_nod(motionProxy)

    #Reads kineticFeedback File
    stop = False
    kinetic_feedbackfile = open('../output/kinetic_feedback.txt', 'r')

    while not stop:
        where = kinetic_feedbackfile.tell()
        line = kinetic_feedbackfile.readline()
        syncwhere = syncFile.tell()
        syncline = syncFile.readline()
        #Checks for new inputs into kinect file
        if not line or line in ['\n','\n']:
            time.sleep(1)
            kinetic_feedbackfile.seek(where)
            gesture_9_nod(motionProxy) #Goes to listening state
        else:
            #if kinetic feedback output file changes
            print "perform function"
            if line.rstrip('\n') != 0:
                #do output
                # decode_input(line.rstrip('\n'),robotIP)
            
                char  = int(line.rstrip('\n'))
                if char == 1:
                    gesture_1_handwave(motionProxy)
                    print "handwave gesture"

                elif char == 2:
                    gesture_2_attention(motionProxy)
                    print "attention"

                elif char == 3:
                    gesture_3_leaning(motionProxy)
                    print "leaning"

                elif char == 4:
                    gesture_4_shrugging(motionProxy)
                    print "shrugging"

                elif char ==5:
                    gesture_5_arms(motionProxy)
                    print "raise up and down"

                elif char ==6:
                    gesture_6_bored(motionProxy)
                    print "Bored"                    

                elif char ==7:
                    gesture_7_coverears(motionProxy)
                    print "Cover ears"                    

                elif char ==8:
                    gesture_8_tilt_head(motionProxy)
                    print "tilt head"                    

                else:
                    gesture_9_nod(motionProxy)
                    print "Nodding Head and standing chill" 

        if not syncline or syncline in ['\n','\n']:
            time.sleep(1)
            syncFile.seek(syncwhere)
        else:
            if syncline.rstrip('\n') == "stop":
                stop = True
            

    animatedSpeechProxy.say("End Presentation - Well Done!", gesture_confused)
    print "End Presentation"


    print "Begin Post-Speech Feedback"

    # postspeech_feedbackfile = open('../output/postspeech_feedback.txt', 'r')    
    
    # data=postspeech_feedbackfile.read()

    # animatedSpeechProxy.say(data, gesture_confused)

    print "End Post-Speech Feedback, Terminating Robot"








    gesture_confused(robotIP)
    StandUp(postureProxy)

    ttsProxy.say("Shut up weicong")

    StandUp(postureProxy)

    squat(robotIP)

    SitDown(postureProxy)

    StiffnessOff(motionProxy)

    motionProxy.rest()


if __name__ == "__main__":
    robotIp = "169.254.62.202" #Set a default IP here
    # robotIp = "127.0.0.1" #Set a default IP here
    robotPort = 9559 #Set default POort here


    # if len(sys.argv) < 2:
    #     print "Usage python robotIP please"
    # else:
    #     robotIp = sys.argv[1]

    # if len(sys.argv) > 2:
    #     print "Usage python robotPort please"
    # else:
    #     robotPort = int(sys.argv[2])

    main(robotIp, robotPort)