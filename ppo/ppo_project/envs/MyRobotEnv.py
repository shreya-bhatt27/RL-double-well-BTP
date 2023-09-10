import numpy as np
import os
from gym import utils, error, spaces
from gym.envs.mujoco import mujoco_env
from mujoco_py import MjViewer, functions

class EnvClassName(mujoco_env.MujocoEnv, utils.EzPickle):
    def __init__(self):
        utils.EzPickle.__init__(self)
        FILE_PATH = 'classic.xml' # Absolute path to your .xml MuJoCo scene file 
                        # OR.
        # FILE_PATH = os.path.join(os.path.dirname(__file__), "MyRobot.xml")
        frame_skip = 5
        mujoco_env.MujocoEnv.__init__(self, FILE_PATH, frame_skip)

    def step(self, a):
        # Carry out one step 
        # Don't forget to do self.do_simulation(a, self.frame_skip)

    def viewer_setup(self):
        # Position the camera

    def reset_model(self):
        # Reset model to original state. 
        # This is called in the overall env.reset method
        # do not call this method directly. 

    def _get_obs(self):
      # Observation of environment fed to agent. This should never be called
      # directly but should be returned through reset_model and step
