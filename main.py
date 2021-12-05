from robot import *
import config
import time

pepper = Pepper(config.IP_ADDRESS, config.PORT)


class PepperProject(object):

    def __init__(self):
        super(PepperProject, self).__init__()
        self.pepper_has_ball = False

    def intro_act(self):
        # Assume Pepper is asleep and we wake it up
        pepper.stand()

        # Pepper greets the room
        robotName = pepper.get_robot_name()
        pepper.say("Hello everyone, my name is %s. Today we will be playing a game together." % robotName)

        # Pepper explains the task
        pepper.start_animation("Explain_1")
        pepper.say("It will be a simple game of throwing and catching a ball.")
        pepper.start_animation("BodyTalk_9")
        pepper.say("For this I will need a volunteer to play.")
        pepper.start_animation("Please_1")
        pepper.say("I hope someone is willing to play catch with me.")


    # def on_right_back_touched_handler(self, value):
    #     if value == 0.0:
    #         return
    #     print("Callback called")
    #     pepper.motion_service.angleInterpolationWithSpeed("RHand", 0.0, 1)
    #     self.pepper_has_ball = True

    def explain_task_instructions(self):
        # pepper.start_animation("Me_1")
        pepper.say("I will raise the hand gently and where you can place the ball");
        pepper.say("Then I will throw the ball from where I stand so you can catch it.")

    def pick_volunteeer(self):
        pepper.pick_a_volunteer(detect_face_props=False)

    def main_act(self):
        speed = 0.1
        self.pepper_has_ball = False

        # Raise a hand to human
        # print("raising hand to human")
        # subscriber = pepper.memory_service.subscriber("HandRightBackTouched")
        # subscriber.signal.connect(self.on_right_back_touched_handler)

        pepper.motion_service.angleInterpolationWithSpeed(["RShoulderPitch", "RWristYaw", "RHand"], [0.4, 3.0, 0.8],
                                                          0.05)
        pepper.motion_service.angleInterpolationWithSpeed("RHand", 0.0, 0.05)

        # Get hand down
        pepper.motion_service.angleInterpolationWithSpeed(["RShoulderPitch", "RWristYaw"], [-1.5, -1.5],
                                                          speed)

        # Throw a ball
        pepper.motion_service.angleInterpolationWithSpeed(["RShoulderPitch", "RWristYaw"], [1.0, -1.5], 1, _async=True)
        pepper.motion_service.angleInterpolationWithSpeed("RHand", 0.8, 1)
        pepper.stand()

    def test(self):
        pepper.stand()
        pepper.move_forward(0.5)
        time.sleep(2)
        pepper.turn_around(1)
        time.sleep(2)
        pepper.stop_moving()
        pepper.stand()


try:
    pepperProject = PepperProject()
    pepperProject.intro_act()
    pepperProject.pick_volunteeer()
    pepperProject.explain_task_instructions()
    time.sleep(1)
    pepperProject.main_act()
except Exception as error:
    print(error)
    pepper.say("I am not sure what to say")
