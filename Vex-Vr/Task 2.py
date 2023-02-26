#region VEXcode Generated Robot Configuration
import math
import random
from vexcode_vr import *

# Brain should be defined by default
brain=Brain()

drivetrain = Drivetrain("drivetrain", 0)
pen = Pen("pen", 8)
pen.set_pen_width(THIN)
left_bumper = Bumper("leftBumper", 2)
right_bumper = Bumper("rightBumper", 3)
front_eye = EyeSensor("frontEye", 4)
down_eye = EyeSensor("downEye", 5)
front_distance = Distance("frontdistance", 6)
distance = front_distance
magnet = Electromagnet("magnet", 7)
location = Location("location", 9)

x_pos = 0
y_pos = 0
MIN_POS = -9
MAX_POS = 9

#endregion VEXcode Generated Robot Configuration
# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:      2023/02/23
#	Description:  Task 1 Template
# 
# ------------------------------------------

def driveXDistance(setpoint,duration):
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        currX_location = location.position(X,MM)
        error = setpoint - currX_location
        k = 2
        speed = k*error
        if(speed > 100):
            speed = 100
        if(speed < -100):
            speed = -100
        drivetrain.set_drive_velocity(speed,PERCENT)
        if(currX_location < setpoint):
            drivetrain.drive(FORWARD)
        elif(currX_location > setpoint):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()
        









        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()

def driveYDistance(setpoint,duration):
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        currY_location = location.position(Y,MM)
        error = setpoint - currY_location
        k = 2
        speed = k*error

        if(speed > 100):
            speed = 100
        if(speed < -100):
            speed = -100



        drivetrain.set_drive_velocity(speed,PERCENT)
        if(currY_location < setpoint):
            drivetrain.drive(FORWARD)
        elif(currY_location > setpoint):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()
        
        









        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()


def driveDiagDistance(setpoint,duration):
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        currY_location = location.position(Y,MM)
        error = setpoint - currY_location
        k = 2
        speed = k*error
        if(speed > 100):
            speed = 100
        if(speed < -100):
            speed = -100

        
        drivetrain.set_drive_velocity(speed,PERCENT)
        if(currY_location < setpoint):
            drivetrain.drive(FORWARD)
        elif(currY_location > setpoint):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()
        









        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()

def rand_pos():
    x_pos = random.randint(MIN_POS, MAX_POS) * 100
    y_pos = random.randint(MIN_POS, MAX_POS) * 100
    return x_pos, y_pos



def drive_to_y(y_pos):
    while location.position(Y,MM) != y_pos:
        if location.position(Y,MM) < y_pos:
            drivetrain.drive(FORWARD)
            wait(5,MSEC)
        if location.position(Y,MM) > y_pos:
            drivetrain.drive(REVERSE)
            wait(5,MSEC)
    drivetrain.stop()


def drive_to_x(x_pos):
    while location.position(X,MM) != x_pos:
        if location.position(X,MM) < x_pos:
            drivetrain.drive(FORWARD)
            wait(5,MSEC)
        if location.position(X,MM) > x_pos:
            drivetrain.drive(REVERSE)
            wait(5,MSEC)
    drivetrain.stop()




# Add project code in "main"
def main():
    x_pos, y_pos = rand_pos()
    brain.print("x:pos", x_pos)
    brain.print("y:pos", y_pos)

    pen.move(DOWN)
    drive_to_y(y_pos)
    drivetrain.turn_to_heading(90,DEGREES,wait=True)
    drive_to_x(x_pos)
    
    
    
# VR threads — Do not delete
vr_thread(main())
