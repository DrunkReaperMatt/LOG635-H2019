'''
Program defining cube tapping interaction

Checks if a LightCube is tapped once, twice or thrice.
'''

import cozmo
import asyncio


async def get_interaction(cube: cozmo.objects.LightCube):
    '''
    Get answer from tapping a cube
    1 tap = yes
    2 taps = no
    3 taps = maybe

    :param cube: a LightCube
    :return: amount of times the lightCube has been tapped (max 3)
    '''
    tap_amount = 0

    try:
        print("Waiting for cube to be tapped")
        await cube.wait_for_tap(timeout=5)
        print("Cube tapped once")
        tap_amount += 1
        await cube.wait_for_tap(timeout=5)
        print("Cube tapped twice")
        tap_amount += 1
        await cube.wait_for_tap(timeout=5)
        print("Cube tapped thrice")
        tap_amount += 1
    finally:
        return tap_amount
