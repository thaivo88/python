import time
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

# method name cozmo_program | class: robot | robot name: cozmo.robot.Robot
def cozmo_program(robot: cozmo.robot.Robot):

    # command cozmo to talk
    # 'wait_for_completed()' syntax complete the statement before moving to the next line
    robot.say_text("Hello World").wait_for_completed()

    # A "for loop" runs for each value i in the given range - in this example
    # starting from 0, while i is less than 5 (so 0,1,2,3,4).
    for i in range(5):
        # Add 1 to the number (so that we count from 1 to 5, not 0 to 4),
        # then convert the number to a string and make Cozmo say it.
        robot.say_text(str(i+1)).wait_for_completed() 
    
    # Drive forwards for X millimeters at X millimeters-per-second.
    # X = any integer
    robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()

    # Turn 90 degrees to the left.
    # Note: To turn to the right, just use a negative number.
    robot.turn_in_place(degrees(90)).wait_for_completed()
    
    # Use a "for loop" to repeat the indented code 4 times
    # Note: the _ variable name can be used when you don't need the value
    for _ in range(4):
        robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
        robot.turn_in_place(degrees(90)).wait_for_completed()

    # Tell the head motor to start lowering the head (at 5 radians per second)
    robot.move_head(-5)
    # Tell the lift motor to start lowering the lift (at 5 radians per second)
    robot.move_lift(-5)
    # Tell Cozmo to drive the left wheel at 25 mmps (millimeters per second),
    # and the right wheel at 50 mmps (so Cozmo will drive Forwards while also
    # turning to the left
    robot.drive_wheels(25, 50)

    # wait for 3 seconds (the head, lift and wheels will move while we wait)
    time.sleep(3)

# to excute the method
cozmo.run_program(cozmo_program)
