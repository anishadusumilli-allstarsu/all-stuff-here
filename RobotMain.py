""" System Files """
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Icon, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase, GyroDriveBase
from pybricks.tools import wait, StopWatch

""" Our files """
import MineStemLib 
from RobotHeart import RobotHeart
from DudeWhoWillRunMyAssignments import DudeWhoWillRunMyAssignments
from RobotAssignment import RobotAssignment
from RobotRun1 import RobotRun1

#--- Robot Configuration -----------------------------------------
#Proportional Integral Derivative (PID) Control with Proportional Constant KP
#This is the value to which the robot turns greater or lesser based on size/friction/etc
TURN_PID_KP = 0
STRAIGHT_PID_KP = 0

left_wheel_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_wheel_motor = Motor(Port.B, Direction.CLOCKWISE)
left_attachment = Motor(Port.C, Direction.CLOCKWISE)
right_attachment = Motor(Port.D, Direction.CLOCKWISE)

#Diameter of the wheels in mm
wheel_dia = 57

#The wheels axle track size. This is the distance in mm between the
#two points where both the wheels touch the ground
wheel_axle_dist = 136

#Default Drive Base speed and acceleration settings
#The initial SYSTEM values are automatically configured based on your wheel diameter 
#and axle track. They are selected such that your robot drives at 
#about 40% of its maximum speed.
#-------------------------------------------------------------

myPrimeHub = PrimeHub()
myRobotHeart = RobotHeart()
myDudeWhoWillRunMyAssignments = DudeWhoWillRunMyAssignments

drive_base = GyroDriveBase(left_wheel_motor, right_wheel_motor, wheel_diameter=wheel_dia, axle_track=wheel_axle_dist)
#default speed and acceleration for going straight and for turning
#we can also set the accleration and decelration separately if we want by providing two values
#for acceleration rather than one
#---- The initial SYSTEM values are automatically configured based on your wheel diameter 
#and axle track. They are selected such that your robot drives at 
#about 40% of its maximum speed.

""" Menu
"""
pressed = []
run_number = 1
myPrimeHub.display.char(str(run_number))
last_buttons = ()

def run1():
    drive_base.straight(500, then=Stop.HOLD, wait=True)
    drive_base.straight(-500, then=Stop.HOLD, wait=True)
    drive_base.turn(90, then=Stop.HOLD, wait=True)
    drive_base.turn(-90, then=Stop.HOLD, wait=True)

def run2():
    drive_base.straight(50)
    #run at 500 degrees/sec to 90 degrees
    left_attachment.run_angle(500,90)
    right_attachment.run(500, 180)
    right_attachment.run(500, -90)

def run3():
    drive_base.straight(50)

def run4():
    drive_base.straight(50)

def run5():
    drive_base.straight(50)

""" Permanent loop to process any button that is pressed """
while True:
    buttons = myPrimeHub.buttons.pressed()
    released_buttons = set(last_buttons) - set(buttons)

    """ Process the button that was pressed """
    if (Button.LEFT in released_buttons):
        run_number = run_number + 1
        if run_number > 5:
            run_number = 1
    myPrimeHub.display.char(str(run_number))
    
    if (Button.RIGHT in released_buttons):
        if run_number == 1:
                run_number = run_number + 1
                run1()
        elif run_number == 2:
                run_number = run_number + 1
                run2()
        elif run_number == 3:
                run_number = run_number + 1
                run3()
        elif run_number == 4:
                run_number = run_number + 1
                run4()
        elif run_number == 5:
                run_number = 1
                run5()
            #cur_run = RobotRun1()
            #run_number = cur_run.doit()
            #myPrimeHub.display.char(str(run_number))
        

    last_buttons = buttons
