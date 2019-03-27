import cozmo
import asyncio
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes
from cozmo.util import distance_mm, speed_mmps

LOOK_AROUND_STATE = 'look_around'
CLUE_FOUND_STATE = 'clue_found'
IS_INVESTIGATING_STATE = 'is_investigating'

class CozmoSherlock:

    def __init__(self, robot: cozmo.robot.Robot):
        self.robot = robot
        self.robot.camera.image_stream_enabled = True
        self.robot.add_event_handler(cozmo.objects.EvtObjectTapped, self.on_tap_cube)
        self.robot.add_event_handler(cozmo.objects.EvtObjectAppeared, self.on_clue_found)

        self.interaction_cube = None # type: LightCube
        self.killer_cube = None # type: LightCube
        self.victim_cube = None # type: LightCube
        self.knife = None

        self.state = LOOK_AROUND_STATE

        self.look_around_behavior = None # type: LookAroundInPlace

    async def on_tap_cube(self, evt, obj, **kwargs):
        if obj.object_id == self.interaction_cube.object_id and self.state != IS_INVESTIGATING_STATE:
            interaction = await self.tap_cube_answer()
            print(interaction)

    async def tap_cube_answer(self):
        tap_amount = 0
        self.state = IS_INVESTIGATING_STATE
        try:
            await self.interaction_cube.wait_for_tap(timeout=5)
            print("Cube tapped once")
            tap_amount = 1
            await self.interaction_cube.wait_for_tap(timeout=5)
            print("Cube tapped twice")
            tap_amount = 2
            await self.interaction_cube.wait_for_tap(timeout=5)
            print("Cube tapped thrice")
            tap_amount = 3
        finally:
            self.state = LOOK_AROUND_STATE
            return tap_amount

    def define_cubes(self):
        self.interaction_cube.set_lights(cozmo.lights.blue_light)
        self.killer_cube.set_lights(cozmo.lights.red_light)
        self.victim_cube.set_lights(cozmo.lights.white_light)

    def connect_cubes(self):
        self.interaction_cube = self.robot.world.get_light_cube(cozmo.objects.LightCube1Id)
        self.killer_cube = self.robot.world.get_light_cube(cozmo.objects.LightCube2Id)
        self.victim_cube = self.robot.world.get_light_cube(cozmo.objects.LightCube3Id)
        return not (self.interaction_cube == None or self.killer_cube == None or self.victim_cube == None)

    async def on_clue_found(self, evt, obj, **kwargs):
        if isinstance(obj, CustomObject):
            print(self.state)
            if self.state == LOOK_AROUND_STATE:
                self.state = CLUE_FOUND_STATE
                if self.look_around_behavior:
                    self.look_around_behavior.stop()
                    self.look_around_behavior = None
            await self.robot.say_text("What is this?").wait_for_completed()

    async def define_known_obj(self):
        self.knife = await self.robot.world.define_custom_wall(CustomObjectTypes.CustomType00,
                                                               CustomObjectMarkers.Circles2,
                                                               40, 40,
                                                               30, 30, True)

    async def look_around(self):
        if self.look_around_behavior == None or not self.look_around_behavior.is_active:
            await asyncio.sleep(.5)
            if self.state == LOOK_AROUND_STATE:
                self.look_around_behavior = self.robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)

    def investigate_clue(self):
        print("investigating...")

    async def run(self):
        if not self.connect_cubes():
            print('Cubes did not connect successfully.')
            return
        self.define_cubes()
        await self.define_known_obj()

        # Updates self.state and resets self.amount_turned_recently every 1 second.
        while True:
            await asyncio.sleep(1)
            if self.state == LOOK_AROUND_STATE:
                await self.look_around()
            if self.state == CLUE_FOUND_STATE:
                self.investigate_clue()


async def cozmo_program(robot: cozmo.robot.Robot):
    investigation = CozmoSherlock(robot)
    await investigation.run()


if __name__ == '__main__':
    cozmo.run_program(cozmo_program, use_3d_viewer=True, show_viewer_controls=True, use_viewer=True)
