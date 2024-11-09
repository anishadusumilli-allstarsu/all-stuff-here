""" System Files """
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Icon, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

""" Our files """
from RobotHeart import RobotHeart
from DudeWhoWillRunMyAssignments import DudeWhoWillRunMyAssignments
from RobotAssignment import RobotAssignment
from RobotRun1 import RobotRun1

myPrimeHub = PrimeHub()
myRobotHeart = RobotHeart()
myDudeWhoWillRunMyAssignments = DudeWhoWillRunMyAssignments

left_wheel_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_wheel_motor = Motor(Port.B, Direction.CLOCKWISE)
left_attachment_motor = Motor(Port.C)
right_attachment_motor = Motor(Port.D)

#Diameter of the wheels in mm
wheel_dia = 57
#The wheels axle track size. This is the distance in mm between the
#two points where both the wheels touch the ground
wheel_axle_dist = 136
drive_base = DriveBase(left_wheel_motor, right_wheel_motor, wheel_diameter=wheel_dia, axle_track=wheel_axle_dist)

""" Menu
"""
pressed = []
run_number = 1
myPrimeHub.display.char(str(run_number))
last_buttons = ()

def run1():
    leftAttachment(-500)

def run2():
    rightAttachment(-500)

def run3():
    drive_base.straight(50)

def run4():
    drive_base.straight(50)

def run5():
    drive_base.straight(50)

def leftAttachment(length):
    left_attachment_motor.run(length)

def rightAttachment(length2):
    right_attachment_motor.run(length2)


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
                run1()
        elif run_number == 2:
                run2()
        elif run_number == 3:
                run3()
        elif run_number == 4:
                run4()
        elif run_number == 5:
                run5()
        
            #cur_run = RobotRun1()
            #run_number = cur_run.doit()
            #myPrimeHub.display.char(str(run_number))
        

    last_buttons = buttons
