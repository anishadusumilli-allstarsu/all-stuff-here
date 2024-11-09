""" System Files """
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

""" Our files """
from RobotHeart import RobotHeart
from RobotAssignment import RobotAssignment

""" We put multiline comments inside Triple Quotes
    Object Class Name: DudeWhoWillRunMyAssignments
    Any time you want you can create an instance of this Dude and have him
    do what you need.
    This Dude needs a pointer to the RobotHeart he is working with
    This dude manages and runs all the RobotAssignments we want to do.
    He lets us 'add' an assignment to the list of assignments we want to run
    He lets us 'deleteAll' or remove all the assignments from our assignment list
    He lets us 'run' all the assignments we created in the assignment list 
"""
class DudeWhoWillRunMyAssignments:
    def __init__(self, RobotHeart):
        self._assignments = []
        self._RobotHeart = RobotHeart

    def addAssignment(self, RobotAssignment):
        """Add new assignment to the assignment list."""
        self._assignments.append(RobotAssignment)
        return RobotAssignment

    def deleteAllAssignments(self):
        """ Delete all the assignments we have added to the assignment list. 
            Stop them if they are running and delete them.
        """
        self._assignments.clear()
    
    def getAssignments(self):
        """Returns all assignments in the list."""
        return self._assignments

    def runAllAssignments(self):
        """Run all assignments in the list."""
        for curRobotAssignment in self._assignments:
            try: next(curRobotAssignment)
            except StopIteration:
                self._assignments.remove(curRobotAssignment)
