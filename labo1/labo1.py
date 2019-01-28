import sys
import time

import cozmo.robot
from cozmo.objects import CustomObjectMarkers,FixedCustomObject,EvtObjectLocated,CustomObjectTypes, CustomObject,\
    EvtObjectAppeared,EvtObjectDisappeared
from cozmo.world import World,CameraImage,EvtNewCameraImage
from PIL import Image, ImageDraw
from cozmo.util import degrees, distance_mm, speed_mmps
from cozmo.audio import AudioEvents
from cozmo.camera import EvtNewRawCameraImage



def handle_object_appeared(evt, **kw):
    if isinstance(evt.obj, CustomObject):
        print("Cozmo started seeing a %s" % str(evt.obj.object_type))


def handle_object_disappeared(evt, **kw):
    # This will be called whenever an EvtObjectDisappeared is dispatched -
    # whenever an Object goes out of view.
    if isinstance(evt.obj, CustomObject):
        print("Cozmo stopped seeing a %s" % str(evt.obj.object_type))


def take_picture(robot: cozmo.robot.Robot, i):
    robot.camera.image_stream_enabled = True
    robot.camera.enable_auto_exposure()
    robot.camera.color_image_enabled = True
    new_image = robot.world.wait_for(cozmo.world.EvtNewCameraImage)
    new_image.image.raw_image.convert().save(str(i) + '.png')
    # new_image.image.raw_image.convert().save("./images/" + str(i) + '.png')


# def markers_recognition(robot : cozmo.robot.Robot):
#    #Circles2 = CustomObjectMarker(name='Circles2', id=0)
#
#    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
#    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)
#
#    circles2 = CustomObjectMarkers.Circles2
#    circles3 = CustomObjectMarkers.Circles3
#    diamonds2 = CustomObjectMarkers.Diamonds2
#    diamonds3 = CustomObjectMarkers.Diamonds3
#    triangle2 = CustomObjectMarkers.Triangles2
#    triangle3 = CustomObjectMarkers.Triangles3
#    triangle3 = CustomObjectMarkers.Triangles4
#    hexagone2 = CustomObjectMarkers.Hexagons2
#    hexagone3 = CustomObjectMarkers.Hexagons3
#
#    markers_identification = robot.world.define_custom_wall(CustomObject.)

def start_music(robot: cozmo.robot.Robot):
    MusicCube = cozmo.audio.AudioEvents(name='MusicCubeWhack', id=3324716189)


# Desempile 2 cubes

def desempileCube(robot : cozmo.robot.Robot):
    # allume les 2 cubes qui seront utilise
    cozmo.objects.LightCube1Id = 1
    cozmo.objects.LightCube2Id = 2
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=2, object_type=cozmo.objects.LightCube, timeout=60)
    lookaround.stop()

    if len(cubes) < 2:
        print("besoin de deux cubes")
        return
    else:
        # Prend le premier cube
        current_action = robot.pickup_object(cubes[0], num_retries=4)
        current_action.wait_for_completed()
        if current_action.has_failed:
            code, reason = current_action.failure_reason
            result = current_action.result
            print("Pickup Cube failed: code=%s reason='%s' result=%s" % (code, reason, result))
            return

        # Depose le cube
        robot.turn_in_place(degrees(90)).wait_for_completed()
        current_action = robot.place_object_on_ground_here()
        current_action.wait_for_completed()
        if current_action.has_failed:
            code, reason = current_action.failure_reason
            result = current_action.result
            print("Place On Cube failed: code=%s reason='%s' result=%s" % (code, reason, result))
            return

        print("Cozmo successfully stacked 2 blocks!")
        return


#empile 2 cubes

def empileCube(robot : cozmo.robot.Robot):
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=2, object_type=cozmo.objects.LightCube, timeout=60)
    lookaround.stop()

    if len(cubes) < 2:
        print("Error: need 2 Cubes but only found", len(cubes), "Cube(s)")
    else:
        # Prend le premier cube
        current_action = robot.pickup_object(cubes[0], num_retries=3)
        current_action.wait_for_completed()
        if current_action.has_failed:
            code, reason = current_action.failure_reason
            result = current_action.result
            robot.say_text("no cube here").wait_for_completed()
            print("Pickup Cube failed: code=%s reason='%s' result=%s" % (code, reason, result))
            return

        # Depose le premier cube sur le deuxieme cube
        current_action = robot.place_on_object(cubes[1], num_retries=3)
        current_action.wait_for_completed()
        if current_action.has_failed:
            code, reason = current_action.failure_reason
            result = current_action.result
            print("Place On Cube failed: code=%s reason='%s' result=%s" % (code, reason, result))
            return

        print("Cozmo successfully stacked 2 blocks!")


def cozmo_program(robot: cozmo.robot.Robot):

    circles2 = CustomObjectMarkers.Circles2
    circles3 = CustomObjectMarkers.Circles3
    diamonds2 = CustomObjectMarkers.Diamonds2
    diamonds3 = CustomObjectMarkers.Diamonds3
    triangle2 = CustomObjectMarkers.Triangles2
    triangle3 = CustomObjectMarkers.Triangles3
    triangle3 = CustomObjectMarkers.Triangles4
    hexagone2 = CustomObjectMarkers.Hexagons2
    hexagone3 = CustomObjectMarkers.Hexagons3

    # Arret 1
    markers_identification = robot.world.define_custom_wall(CustomObjectTypes.CustomType00,circles2 ,120, 100,50, 30, True)
    take_picture(robot, 1)
    print(markers_identification)
    robot.drive_straight(distance_mm(90), speed_mmps(50)).wait_for_completed()
    print('1')
    # Arret 2 (parcours losange)
    robot.say_text(" La premiere action est de dire un texte").wait_for_completed()
    take_picture(robot, 2)
    robot.drive_straight(distance_mm(90), speed_mmps(50)).wait_for_completed()
    start_music(robot)
    print('2')
    # Arret 3
    take_picture(robot, 3)
    robot.drive_straight(distance_mm(90), speed_mmps(50)).wait_for_completed()
    print('3')
    # Arret 4 (parcours losange)
    take_picture(robot, 4)
    robot.drive_straight(distance_mm(90), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
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
    # Arret 9 (parcours losange)
    robot.drive_straight(distance_mm(90), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    take_picture(robot, 9)
    print('9')
    # Arret 10
    robot.drive_straight(distance_mm(80), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    take_picture(robot, 10)
    print('10')
    # Arret 11 (parcours losange)
    robot.drive_straight(distance_mm(80), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    take_picture(robot, 11)
    print('11')
    # Arret 12
    robot.drive_straight(distance_mm(80), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    take_picture(robot, 12)
    print('12')
    # Arret 13 (parcours losange)
    robot.drive_straight(distance_mm(80), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    take_picture(robot, 13)
    print('13')
    # Arret 14
    robot.drive_straight(distance_mm(80), speed_mmps(50)).wait_for_completed()
    take_picture(robot, 14)
    print('14')
    # Arret 15 (parcours losange)
    robot.drive_straight(distance_mm(80), speed_mmps(50)).wait_for_completed()
    take_picture(robot, 15)
    print('15')


if __name__ == '__main__':
    cozmo.run_program(cozmo_program)
