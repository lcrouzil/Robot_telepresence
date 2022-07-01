#!/usr/bin/env python3

import rospy
import std_msgs.msg
import RPi.GPIO as GPIO

key = ""

def essaie(data):
    global key
    key = data.data

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(3, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(3, False)
	pwm.ChangeDutyCycle(0)

def main():
    global key
    rospy.init_node("camera")
    sub = rospy.Subscriber('key_app',std_msgs.msg.String,essaie)
    local_key = ""
    rate = rospy.Rate(10)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.OUT)
    GPIO.remove_event_detect(3)
    pwm=GPIO.PWM(3, 50)
    pwm.start(0)
    
    while not rospy.is_shutdown():

        if (local_key != key):
            print(local_key)
            print(key)
            local_key = key
            key = ""
        if(local_key == "up"):
            print("Coucoiu")
            SetAngle(90) 
        elif(local_key == "down"):
            print("bouh")
            SetAngle(0) 
        rate.sleep()
    pwm.stop()
    GPIO.cleanup()


main()
