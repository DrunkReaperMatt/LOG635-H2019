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


def cozmo_program(robot: cozmo.robot.Robot):
    print("Starting Investigation")


if __name__ == '__main__':
    cozmo.run_program(cozmo_program, use_3d_viewer=True, show_viewer_controls=True)
