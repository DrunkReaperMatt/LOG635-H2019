import sys
import time

import cozmo
import cozmo.robot
import asyncio
from cozmo.objects import CustomObjectMarkers,FixedCustomObject,EvtObjectLocated,CustomObjectTypes, CustomObject,\
    EvtObjectAppeared,EvtObjectDisappeared
from cozmo.world import World,CameraImage,EvtNewCameraImage
from PIL import Image, ImageDraw
from cozmo.util import degrees, distance_mm, speed_mmps
from cozmo.audio import AudioEvents
from cozmo.camera import EvtNewRawCameraImage

import labo3.interactions.tap as tap
# import labo3.interactions.marker as marker


def handle_object_appeared(evt, **kw):
    # This will be called whenever an EvtObjectAppeared is dispatched -
    # whenever an Object comes into view.
    if isinstance(evt.obj, CustomObject):
        print("Cozmo started seeing a %s" % str(evt.obj.object_type))
        marker_interaction(evt.obj)


def handle_object_disappeared(evt, **kw):
    # This will be called whenever an EvtObjectDisappeared is dispatched -
    # whenever an Object goes out of view.
    if isinstance(evt.obj, CustomObject):
        print("Cozmo stopped seeing a %s" % str(evt.obj.object_type))


def custom_objects(robot: cozmo.robot.Robot):
    circle2 = robot.world.define_custom_wall(CustomObjectTypes.CustomType00,
                                             CustomObjectMarkers.Circles2,
                                             50, 50,
                                             50, 50, True)


def marker_interaction(robot, object):
    action = cozmo.robot.Robot.go_to_object(object, distance_mm(70.0))
    action.wait_for_completed()
    cozmo.robot.Robot.say_text("What is this?").wait_for_completed()


def cozmo_program(robot: cozmo.robot.Robot):
    print("Starting Investigation")
    robot.add_event_handler(robot, cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)

    cube = None
    knife = custom_objects(robot)

    look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)

    try:
        cube = robot.world.wait_for_observed_light_cube(timeout=60)
    except asyncio.TimeoutError:
        print("Didn't find a cube :-(")
        return
    finally:
        look_around.stop()

    if cube:
        interaction = tap.get_interaction(cube)
        print(interaction)


if __name__ == '__main__':
    cozmo.run_program(cozmo_program, use_3d_viewer=True, show_viewer_controls=True, use_viewer=True)
