#!/usr/bin/env python
# coding:utf-8

import math
import numpy as np
import time
from time import sleep
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from dynamic_reconfigure.server import Server
RAD2DEG = 180 / math.pi

class laserAvoid:
    def __init__(self):
        rospy.on_shutdown(self.cancel)
        self.r = rospy.Rate(20)
        self.Moving = False
        self.switch = False
        self.Right_warning = 0
        self.Left_warning = 0
        self.front_warning = 0
        self.ros_ctrl = ROSCtrl()
        Server(laserAvoidPIDConfig, self.dynamic_reconfigure_callback)
        self.linear = 0.5
        self.angular = 0.8
        self.ResponseDist = 0.45
        self.LaserAngle = 30  # 10~50
        self.ObstacleValidAngle = 4  # valid
        self.sub_laser = rospy.Subscriber('/scan', LaserScan, self.registerScan, queue_size=1)

    def cancel(self):
        self.ros_ctrl.pub_vel.publish(Twist())
        self.ros_ctrl.cancel()
        self.sub_laser.unregister()
        rospy.loginfo("Shutting down this node.")

    def dynamic_reconfigure_callback(self, config, level):
        self.switch = config['switch']
        self.linear = config['linear']
        self.angular = config['angular']
        self.LaserAngle = config['LaserAngle']
        self.ResponseDist = config['ResponseDist']
        return config

    def registerScan(self, scan_data):
        if not isinstance(scan_data, LaserScan): return
        ranges = np.array(scan_data.ranges)
        self.Right_warning = 0
        self.Left_warning = 0
        self.front_warning = 0
        for i in range(len(ranges)):
            angle = (scan_data.angle_min + scan_data.angle_increment * i) * RAD2DEG * 1#-90 90

            if -10 > angle > -10-self.LaserAngle:
                if ranges[i] < self.ResponseDist: 
                    self.Right_warning += 1

            if 10+self.LaserAngle > angle > 10:
                if ranges[i] < self.ResponseDist: 
                    self.Left_warning += 1

            if abs(angle) < 10:
                if ranges[i] <= self.ResponseDist: 
                    self.front_warning += 1

        if self.ros_ctrl.Joy_active or self.switch == True:
            if self.Moving == True:
                self.ros_ctrl.pub_vel.publish(Twist())
                self.Moving = not self.Moving
            return
        self.Moving = True


        valid_num=int(self.ObstacleValidAngle/(scan_data.angle_increment* RAD2DEG))
        twist = Twist()

        if self.front_warning > valid_num and self.Left_warning > valid_num and self.Right_warning > valid_num:
            print ('1, there are obstacles in the left and right, turn right')
            twist.linear.x = -0.15
            twist.angular.z = -self.angular
            self.ros_ctrl.pub_vel.publish(twist)
            sleep(0.2)
        elif self.front_warning > valid_num and self.Left_warning <= valid_num and self.Right_warning > valid_num:
            print ('2, there is an obstacle in the middle right, turn left')
            twist.linear.x = 0
            twist.angular.z = self.angular
            self.ros_ctrl.pub_vel.publish(twist)
            sleep(0.2)
            if self.Left_warning > valid_num and self.Right_warning <= valid_num:
                print ('3, there is an obstacle on the left, turn right')
                twist.linear.x = 0
                twist.angular.z = -self.angular
                self.ros_ctrl.pub_vel.publish(twist)
                sleep(0.5)
        elif self.front_warning > valid_num and self.Left_warning > valid_num and self.Right_warning <= valid_num:
            print ('4. There is an obstacle in the middle left, turn right')
            twist.linear.x = 0
            twist.angular.z = -self.angular
            self.ros_ctrl.pub_vel.publish(twist)
            sleep(0.2)
            if self.Left_warning <= valid_num and self.Right_warning > valid_num:
                print ('5, there is an obstacle on the left, turn left')
                twist.linear.x = 0
                twist.angular.z = self.angular
                self.ros_ctrl.pub_vel.publish(twist)
                sleep(0.5)
        elif self.front_warning > valid_num and self.Left_warning < valid_num and self.Right_warning < valid_num:
            print ('6, there is an obstacle in the middle, turn left')
            twist.linear.x = 0
            twist.angular.z = self.angular
            self.ros_ctrl.pub_vel.publish(twist)
            sleep(0.2)
        elif self.front_warning < valid_num and self.Left_warning > valid_num and self.Right_warning > valid_num:
            print ('7. There are obstacles on the left and right, turn right')
            twist.linear.x = 0
            twist.angular.z = -self.angular
            self.ros_ctrl.pub_vel.publish(twist)
            sleep(0.4)
        elif self.front_warning < valid_num and self.Left_warning > valid_num and self.Right_warning <= valid_num:
            print ('8, there is an obstacle on the left, turn right')
            twist.linear.x = 0
            twist.angular.z = -self.angular
            self.ros_ctrl.pub_vel.publish(twist)
            sleep(0.2)
        elif self.front_warning < valid_num and self.Left_warning <= valid_num and self.Right_warning > valid_num:
            print ('9, there is an obstacle on the right, turn left')
            twist.linear.x = 0
            twist.angular.z = self.angular
            self.ros_ctrl.pub_vel.publish(twist)
            sleep(0.2)
        elif self.front_warning <= valid_num and self.Left_warning <= valid_num and self.Right_warning <= valid_num:
            print ('10, no obstacles, go forward')
            twist.linear.x = self.linear
            twist.angular.z = 0
            self.ros_ctrl.pub_vel.publish(twist)
        self.r.sleep()


if __name__ == "__main__":
    print("init laser_Avoidance")
    rospy.init_node('laser_Avoidance', anonymous=False)
    tracker = laserAvoid()
    rospy.spin()