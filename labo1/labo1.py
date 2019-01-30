import sys
import time

import cozmo.robot
import asyncio
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


def follow_faces(robot: cozmo.robot.Robot):
    '''The core of the follow_faces program'''

    # Move lift down and tilt the head up
    robot.move_lift(-3)
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()

    face_to_follow = None

    while True:
        turn_action = None
        if face_to_follow:
            turn_action = robot.turn_towards_face(face_to_follow)

        if not (face_to_follow and face_to_follow.is_visible):
            # find a visible face, timeout if nothing found after a short while
            try:
                face_to_follow = robot.world.wait_for_observed_face(timeout=5)
            except asyncio.TimeoutError:
                print("Didn't find a face - exiting!")
                return

        if turn_action:
            # Complete the turn action if one was in progress
            turn_action.wait_for_completed()

        time.sleep(.1)


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
    robot.play_audio(cozmo.audio.AudioEvents.Sfx_Egg_Decorating_Crack)
    time.sleep(2.0)


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


def custom_objects(robot: cozmo.robot.Robot):

    circles2 = CustomObjectMarkers.Circles2
    circles3 = CustomObjectMarkers.Circles3
    diamonds2 = CustomObjectMarkers.Diamonds2
    diamonds3 = CustomObjectMarkers.Diamonds3
    triangle2 = CustomObjectMarkers.Triangles2
    triangle3 = CustomObjectMarkers.Triangles3
    triangle4 = CustomObjectMarkers.Triangles4
    hexagone2 = CustomObjectMarkers.Hexagons2
    hexagone3 = CustomObjectMarkers.Hexagons3

    # Add event handlers for whenever Cozmo sees a new object
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)

    # define a unique cube (44mm x 44mm x 44mm) (approximately the same size as a light cube)
    # with a 30mm x 30mm Diamonds2 image on every face
    cube_obj = robot.world.define_custom_cube(CustomObjectTypes.CustomType00,
                                              CustomObjectMarkers.Diamonds2,
                                              44,
                                              30, 30, True)

    # define a unique cube (88mm x 88mm x 88mm) (approximately 2x the size of a light cube)
    # with a 50mm x 50mm Diamonds3 image on every face
    big_cube_obj = robot.world.define_custom_cube(CustomObjectTypes.CustomType01,
                                              CustomObjectMarkers.Diamonds3,
                                              88,
                                              50, 50, True)

    # define a unique wall (150mm x 120mm (x10mm thick for all walls)
    # with a 50mm x 30mm Circles2 image on front and back
    wall_obj = robot.world.define_custom_wall(CustomObjectTypes.CustomType02,
                                              CustomObjectMarkers.Circles2,
                                              150, 120,
                                              50, 30, True)

    # define a unique box (60mm deep x 140mm width x100mm tall)
    # with a different 30mm x 50mm image on each of the 6 faces
    box_obj = robot.world.define_custom_box(CustomObjectTypes.CustomType03,
                                            CustomObjectMarkers.Hexagons2,  # front
                                            CustomObjectMarkers.Circles3,   # back
                                            CustomObjectMarkers.Circles4,   # top
                                            CustomObjectMarkers.Circles5,   # bottom
                                            CustomObjectMarkers.Triangles2, # left
                                            CustomObjectMarkers.Triangles3, # right
                                            60, 140, 100,
                                            30, 50, True)

    if ((cube_obj is not None) and (big_cube_obj is not None) and
            (wall_obj is not None) and (box_obj is not None)):
        print("All objects defined successfully!")
    else:
        print("One or more object definitions failed!")
        return

    print("Show the above markers to Cozmo and you will see the related objects "
          "annotated in Cozmo's view window, you will also see print messages "
          "everytime a custom object enters or exits Cozmo's view.")

    print("Press CTRL-C to quit")
    while True:
        time.sleep(0.1)


def cozmo_program(robot: cozmo.robot.Robot):

    # Arret 1
    take_picture(robot, 1)
    robot.drive_straight(distance_mm(90), speed_mmps(50)).wait_for_completed()
    print('1')
    # Arret 2 (parcours losange)
    robot.say_text(" All your bases are belong to us").wait_for_completed()
    take_picture(robot, 2)
    robot.drive_straight(distance_mm(90), speed_mmps(50)).wait_for_completed()
    print('2')
    # Arret 3
    take_picture(robot, 3)
    robot.drive_straight(distance_mm(90), speed_mmps(50)).wait_for_completed()
    print('3')
    # Arret 4 (parcours losange)
    take_picture(robot, 4)
    start_music(robot)
    robot.drive_straight(distance_mm(90), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    print('4')
    # Arret 5
	#revoir code -- inifinite loop.
    #custom_objects(robot)
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
    follow_faces(robot)
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
    empileCube(robot)
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
    desempileCube(robot)
    robot.drive_straight(distance_mm(80), speed_mmps(50)).wait_for_completed()
    take_picture(robot, 15)
    print('15')


if __name__ == '__main__':
    cozmo.run_program(cozmo_program, use_3d_viewer=True, show_viewer_controls=True)
