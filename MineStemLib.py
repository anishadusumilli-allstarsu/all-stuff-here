""" -------------------------------------------
    MineStem Library for FLL robots:
    - findColor(sensor, low_intensity, high_intensity)
    - myHeading(myHub)
    - resetHeading(myHub)
    -------------------------------------------
"""
#from MineStemLib import resetHeading
#from MineStemLib import myHeading
"""
    Keep looking at color sensor and return when you see the
    intensity is in the range requested
    """
def findColor(sensor, low_intensity, high_intensity):
    while True:
        reflection1 = sensor.reflection()
        if ((reflection1 >= low_intensity) and (reflection1 <= high_intensity)):
            #print(reflection1)
            return
        else:
            #As we cannot have an empty 'else' we use 'pass'
            pass

""" Get the current yaw or heading of the robot relative to
    the starting point. heading is reset to 0 when the program starts.
    heading also becomes wrong when we pick up the robot, so use
    reset_heading to reset it to 0 before every run
    When it turns left the heading is negative. From 0 to -360.
    It goes from 0 to 360 when going right.
    """
def myHeading(myHub):
    return myHub.imu.heading()

def resetHeading(myHub):
    myHub.imu.reset_heading(0)

