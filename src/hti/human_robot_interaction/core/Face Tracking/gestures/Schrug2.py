# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ -0.18719, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ -0.33685, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ -0.33685, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ -0.33685, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ -0.33685, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ -0.18675, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("HeadYaw")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ -0.00464, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ -0.00464, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ -0.00464, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ -0.00464, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ -0.00464, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ -0.00464, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LAnklePitch")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ 0.07052, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ 0.07052, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.07052, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.07052, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ 0.07052, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ 0.07052, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LAnkleRoll")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ -0.10734, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ -0.10734, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ -0.10734, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ -0.10734, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ -0.10734, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ -0.10734, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowRoll")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ -0.58748, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ -1.16588, [ 3, -0.40000, 0.14116], [ 3, 0.26667, -0.09411]], [ -1.29329, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ -1.29329, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ -0.58748, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ -0.58748, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LElbowYaw")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ -1.22724, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ -1.17635, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ -2.08567, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ -2.08567, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ -1.22724, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ -1.22724, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHand")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ 0.00405, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ 0.00405, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.01292, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.01292, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ 0.00405, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ 0.00405, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHipPitch")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ 0.20406, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ 0.20406, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.20406, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.20406, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ 0.20406, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ 0.20406, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHipRoll")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ 0.11202, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ 0.11202, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.11202, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.11202, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ 0.11202, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ 0.11202, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LHipYawPitch")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ -0.16103, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ -0.16103, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ -0.16103, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ -0.16103, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ -0.16103, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ -0.16103, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LKneePitch")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ -0.09055, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ -0.09055, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ -0.09055, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ -0.09055, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ -0.09055, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ -0.09055, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LShoulderPitch")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ 1.59225, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ 1.59225, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ 1.59225, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ 1.59225, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ 1.59225, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ 1.59225, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LShoulderRoll")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ 0.16563, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ 0.16563, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.08378, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.08378, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ 0.16563, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ 0.16563, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("LWristYaw")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ 0.10887, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ 0.39794, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ -1.02800, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ -1.02800, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ 0.10887, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ 0.10887, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RAnklePitch")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ 0.06294, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ 0.06294, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.06294, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.06294, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ 0.06294, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ 0.06294, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RAnkleRoll")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ 0.06600, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ 0.06600, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.06600, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.06600, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ 0.06600, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ 0.06600, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowRoll")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ 0.43570, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ 1.18159, [ 3, -0.40000, -0.19979], [ 3, 0.26667, 0.13319]], [ 1.43466, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ 1.43466, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ 0.43570, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ 0.43570, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RElbowYaw")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ 1.18114, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ 1.18114, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ 2.08567, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ 2.08567, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ 1.18114, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ 1.18114, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHand")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ 0.00710, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ 0.00710, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.01292, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.01292, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ 0.00710, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ 0.00710, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHipPitch")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ 0.18864, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ 0.18864, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.18864, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.18864, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ 0.18864, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ 0.18864, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHipRoll")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ -0.06745, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ -0.06745, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ -0.06745, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ -0.06745, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ -0.06745, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ -0.06745, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RHipYawPitch")
times.append([ 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ -0.16103, [ 3, -1.06667, 0.00000], [ 3, 0.26667, 0.00000]], [ -0.16103, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ -0.16103, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ -0.16103, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ -0.16103, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RKneePitch")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ -0.07359, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ -0.07359, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ -0.07359, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ -0.07359, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ -0.07359, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ -0.07359, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderPitch")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ 1.48649, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ 1.71217, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ 1.53938, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ 1.53938, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ 1.48649, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ 1.48649, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RShoulderRoll")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ -0.11202, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ -0.11202, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ -0.11202, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ -0.11202, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ -0.11202, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ -0.11202, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

names.append("RWristYaw")
times.append([ 2.00000, 3.20000, 4.00000, 5.50000, 6.10000, 7.00000])
keys.append([ [ 0.17330, [ 3, -0.66667, 0.00000], [ 3, 0.40000, 0.00000]], [ 0.17330, [ 3, -0.40000, 0.00000], [ 3, 0.26667, 0.00000]], [ 0.99484, [ 3, -0.26667, 0.00000], [ 3, 0.50000, 0.00000]], [ 0.99484, [ 3, -0.50000, 0.00000], [ 3, 0.20000, 0.00000]], [ 0.17330, [ 3, -0.20000, 0.00000], [ 3, 0.30000, 0.00000]], [ 0.17330, [ 3, -0.30000, 0.00000], [ 3, 0.00000, 0.00000]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys);
except BaseException, err:
  print err
