import sys
import time

import cozmo
from PIL import Image, ImageDraw
from cozmo.util import degrees, distance_mm, speed_mmps
import numpy as np
from cozmo.camera import EvtNewRawCameraImage


def take_picture(robot: cozmo.robot.Robot, i):
    robot.camera.image_stream_enabled = True
    robot.camera.enable_auto_exposure()
    robot.camera.color_image_enabled = True
    new_image = robot.world.wait_for(cozmo.world.EvtNewCameraImage)
    new_image.image.raw_image.convert().save(str(i) + '.png')
    # new_image.image.raw_image.convert().save("./images/" + str(i) + '.png')


def cozmo_program(robot: cozmo.robot.Robot):
    # Arret 1
    robot.drive_straight(distance_mm(90), speed_mmps(50)).wait_for_completed()
    take_picture(robot, 1)
    print('1')
    # Arret 2 (losange)
    robot.say_text(" La premiere action est de dire un texte").wait_for_completed()
    take_picture(robot, 2)
    robot.drive_straight(distance_mm(90), speed_mmps(50)).wait_for_completed()
    print('2')
    # Arret 3
    take_picture(robot, 3)
    robot.drive_straight(distance_mm(90), speed_mmps(50)).wait_for_completed()
    print('3')
    # Arret 4 (losange)
    robot.drive_straight(distance_mm(90), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    take_picture(robot, 4)
    print('4')
    # Arret 5
    robot.drive_straight(distance_mm(90), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    take_picture(robot, 5)
    print('5')
    # Arret 6
    robot.drive_straight(distance_mm(90), speed_mmps(50)).wait_for_completed()
    take_picture(robot, 6)
    print('6')
    # Arret 7
    robot.drive_straight(distance_mm(90), speed_mmps(50)).wait_for_completed()
    take_picture(robot, 7)
    print('7')
    # Arret 8
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.drive_straight(distance_mm(90), speed_mmps(50)).wait_for_completed()
    take_picture(robot, 8)
    print('8')
    # Arret 9 (losange)
    robot.drive_straight(distance_mm(90), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    take_picture(robot, 9)
    print('9')
    # Arret 10
    robot.drive_straight(distance_mm(80), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    take_picture(robot, 10)
    print('10')
    # Arret 11 (losange)
    robot.drive_straight(distance_mm(80), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    take_picture(robot, 11)
    print('11')
    # Arret 12
    robot.drive_straight(distance_mm(80), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    take_picture(robot, 12)
    print('12')
    # Arret 13 (losange)
    robot.drive_straight(distance_mm(80), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    take_picture(robot, 13)
    print('13')
    # Arret 14
    robot.drive_straight(distance_mm(80), speed_mmps(50)).wait_for_completed()
    take_picture(robot, 14)
    print('14')
    # Arret 15 (losange)
    robot.drive_straight(distance_mm(80), speed_mmps(50)).wait_for_completed()
    take_picture(robot, 15)
    print('15')


if __name__ == '__main__':
    cozmo.run_program(cozmo_program)
