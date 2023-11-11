"""
Classic cart-pole system implemented by Rich Sutton et al.
Copied from http://incompleteideas.net/sutton/book/code/pole.c
permalink: https://perma.cc/C9ZM-652R
"""
import math
from typing import Optional, Union

import numpy as np

import gym
from gym import logger, spaces
from gym.envs.classic_control import utils
from gym.error import DependencyNotInstalled


class CartPoleEnv(gym.Env[np.ndarray, Union[int, np.ndarray]]):
    """
    Modified version of cartpole from https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py
    with zero rendering.
    """

    def __init__(self):
        self.gravity = 9.8
        self.masscart = 3.0
        self.masspole = 0.5
        self.total_mass = self.masspole + self.masscart
        self.length = 0.8  # actually half the pole's length
        self.polemass_length = self.masspole * self.length
        self.force_mag = 7.0
        self.tau = 0.02  # seconds between state updates
        self.kinematics_integrator = "euler"


        self.screen_width = 600
        self.screen_height = 400
        self.screen = None
        self.clock = None
        self.isopen = True

        # Set the initial state
        self.x = 0
        self.x_dot = 0
        self.theta = 0
        self.theta_dot = 0


    def step(self, action):
 
        force = self.force_mag if action == 1 else -self.force_mag
        costheta = math.cos(self.theta)
        sintheta = math.sin(self.theta)

        # For the interested reader:
        # https://coneural.org/florian/papers/05_cart_pole.pdf
        temp = (
            force + self.polemass_length * self.theta_dot**2 * sintheta
        ) / self.total_mass
        thetaacc = (self.gravity * sintheta - costheta * temp) / (
            self.length * (4.0 / 3.0 - self.masspole * costheta**2 / self.total_mass)
        )
        xacc = temp - self.polemass_length * thetaacc * costheta / self.total_mass

        if self.kinematics_integrator == "euler":
            self.x = self.x + self.tau * self.x_dot
            self.x_dot = self.x_dot + self.tau * xacc
            self.theta = self.theta + self.tau * self.theta_dot
            self.theta_dot = self.theta_dot + self.tau * thetaacc
        else:  # semi-implicit euler
            self.x_dot = self.x_dot + self.tau * xacc
            self.x = self.x + self.tau * self.x_dot
            self.theta_dot = self.theta_dot + self.tau * thetaacc
            self.theta = self.theta + self.tau * self.theta_dot


