#!/usr/bin/env python3
import os
import random
from .sound import Sound
from pathlib import Path
from mpyg321.mpyg321 import MPyg321Player, PlayerStatus
import pexpect
class Mode(object):

    def __init__(self,config):
        self.config = config

    def run(self):
        Sound(self.config.get("mp3", "../sounds/custom/buzzer.mp3")).play()


    def button_event(self, button_id):
        pass

    def joystick_event(self, direction):
        pass

    def next_profile(self):
        self.current_profile = (self.current_profile+1) % len(self.config["profiles"])

    def previous_profile(self):
        self.current_profile = (self.current_profile - 1) % len(self.config["profiles"])

class TravelMode(Mode):
    def button_event(self, event):
        liste_directions = os.listdir("../sounds/directions/")

        Sound(Path("../sounds/directions/",random.choices(liste_directions)[0])).play()



class SoundboardMode(Mode):

    def __init__(self,config):
        self.config = config
        self.current_profile = 0
        self.player = MPyg321Player()

    def button_event(self, button_id):
        print(button_id)
        if button_id == 6:
            if self.player.status == PlayerStatus.PLAYING:
                self.player.pause()
            else:
                self.player.resume()
        else:
            self.player.play_song(str(Path(self.config["profiles"][self.current_profile]["binding"].get(str(button_id),"../sounds/custom/buzzer.mp3"))))
        #Sound().play()


    def joystick_event(self, direction):

        if direction == "E":
            self.next_profile()
            Sound(Path(self.config["profiles"][self.current_profile]["mp3"])).play()
        elif direction == "W":
            self.previous_profile()
            Sound(Path(self.config["profiles"][self.current_profile]["mp3"])).play()


class QuizzMode(Mode):
    def __init__(self,config):
        self.config = config
        self.state = None
        self.score = 0
        self.question_list = os.listdir("../sounds/quizz_des_enfants/questions/")
        self.true_response = [0,1]
        self.false_response = [2,3]
        self.player = MPyg321Player()


    def start(self):

        Sound("../sounds/quizz_des_enfants/consigne.mp3").play()
        self.state = "RUNNING"
        self.current_question = 0
        self.questions = random.choices(self.question_list,k=2)
        self.play_question()


    def check_reponse(self,button_id):
        if self.questions[self.current_question].startswith('pot') and button_id in self.true_response:
            Sound("../sounds/quizz_des_enfants/bravo.mp3").play()
            self.score += 1
        else:
            Sound("../sounds/quizz_des_enfants/non.mp3").play()
        self.current_question += 1
        if self.current_question >= len(self.questions):
            self.end()

    def end(self):
        Sound(f"../sounds/quizz_des_enfants/points/{self.score}_point.mp3").play()
        self.state = None
        self.current_question = 0
        self.score = 0


    def play_question(self):
        Sound("../sounds/quizz_des_enfants/questions/" + self.questions[self.current_question]).play()

    def button_event(self, button_id):
        print("le quiiz")
        if self.state is None:
            self.start()
        else:
            self.check_reponse(button_id)
            if self.current_question != 0:
                self.play_question()
