#!/usr/bin/env python3

import pygame
from pygame.locals import *
import os
import json
import random
import platform
from pathlib import Path
from lib.mode import TravelMode, SoundboardMode, QuizzMode

if platform.system() in ["Linux", "Darwin"]:
    x_axis = 0
    y_axis = 1
else:
    x_axis = 1
    y_axis = 0

config = {}


class MagicBox(object):

    def __init__(self):
        with open(Path("../config/soundboard.json")) as conf_file:
            self.config = json.load(conf_file)

        self.modes = []
        self.current_mode_index = 0
        self.modes.append(QuizzMode(self.config['modes']["quizzMode"]))

        self.modes.append(TravelMode(self.config['modes']["travelMode"]))
        self.modes.append(SoundboardMode(self.config['modes']["soundboardMode"]))
        print(self.modes)
        # self.current_profile = 0

    @property
    def current_mode(self):
        return self.modes[self.current_mode_index]

    def next_profile(self):
        print("next_profile")
        self.current_profile = (self.current_profile + 1) % len(self.config["profiles"])

    def previous_profile(self):
        self.current_profile = (self.current_profile - 1) % len(self.config["profiles"])

    def next_mode(self):
        self.current_mode_index = (self.current_mode_index + 1) % len(self.modes)

    def previous_mode(self):
        self.current_mode_index = (self.current_mode_index - 1) % len(self.modes)

    #    def get_sound(self,button_id):
    #        return(self.config["profiles"][self.current_profile]["binding"].get(str(button_id),"../sounds/custom/buzzer.mp3"))

    def deal_with_joystick(self, event):
        event.value = round(event.value, 1)
        if event.axis == x_axis:
            if event.value < 0:
                if round(mon_joystick.get_axis(y_axis), 2) < 0:
                    return ('NE')
                elif round(mon_joystick.get_axis(y_axis), 2) > 0:
                    return ('SW')
                else:
                    return ("W")
            elif event.value > 0:
                if round(mon_joystick.get_axis(y_axis), 2) < 0:
                    return ('NE')
                elif round(mon_joystick.get_axis(y_axis), 2) > 0:
                    return ('SE')
                else:
                    return ("E")
            elif event.value == 0:
                if round(mon_joystick.get_axis(y_axis), 2) > 0:
                    self.next_mode()
                    self.current_mode.run()
                    return ('S')

                elif round(mon_joystick.get_axis(y_axis), 2) < 0:
                    self.previous_mode()
                    self.current_mode.run()
                    return ('N')

            elif event.value == 0:
                if round(mon_joystick.get_axis(y_axis), 2) > 0:
                    self.next_mode()
                    self.current_mode.run()
                    return ('S')

                elif round(mon_joystick.get_axis(y_axis), 2) < 0:
                    self.previous_mode()
                    self.current_mode.run()
                    return ('N')
        elif event.axis == y_axis and event.value < 0:
            if round(mon_joystick.get_axis(x_axis), 2) < 0:
                return ('NW')
            elif round(mon_joystick.get_axis(x_axis), 2) > 0:
                return ('NE')
            else:
                self.previous_mode()
                self.current_mode.run()
                return ("N")

        elif event.axis == y_axis and event.value > 0:
            if round(mon_joystick.get_axis(x_axis), 2) < 0:
                return ('SW')
            elif round(mon_joystick.get_axis(x_axis), 2) > 0:
                return ('SE')
            else:
                self.next_mode()
                self.current_mode.run()
                return ("S")
        elif event.axis == y_axis and event.value == 0 and round(mon_joystick.get_axis(x_axis)) > 0:
            return ('E')

        elif event.axis == y_axis and event.value == 0 and round(mon_joystick.get_axis(x_axis), 2) < 0:
            return ('W')


if __name__ == "__main__":

    arisa = MagicBox()
    pygame.init()

    # On compte les joysticks
    nb_joysticks = pygame.joystick.get_count()
    # Et on en cree un s'il y a en au moins un
    if nb_joysticks > 0:
        mon_joystick = pygame.joystick.Joystick(0)

        mon_joystick.init()
        # On compte les boutons
        nb_boutons = mon_joystick.get_numbuttons()
        print(nb_boutons)
        if nb_boutons >= 4:
            continuer = 1
            print("lets's go")
            while continuer:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        continuer = 0
                    if event.type == JOYBUTTONDOWN:
                        arisa.current_mode.button_event(event.button)
                    if event.type == JOYAXISMOTION:
                        direction = arisa.deal_with_joystick(event)
                        arisa.current_mode.joystick_event(direction)


        else:
            print("Votre Joystick ne possède pas au moins 4 boutons")
    else:
        print("Vous n'avez pas branché de Joystick...")
