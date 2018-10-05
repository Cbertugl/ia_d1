#!/usr/bin/python

import threading
import time
import environment as epy
import agent as apy
import random
import search as sc


class agentThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.robot = apy.Agent(5, 5)
        self.env = None

    def run(self):
        print("Agent running")
        while(1):
            # TODO: algorithme de l'agent
            rand = random.randint(0,9)
            text = "Aspirobot T-0.1 moving "
            if(rand == 0 or rand == 1):
                text += "up"
                self.robot.move("up", self.env)
            if(rand == 2 or rand == 3):
                text += "down"
                self.robot.move("down", self.env)
            if(rand == 4 or rand == 5):
                text += "left"
                self.robot.move("left", self.env)
            if(rand == 6 or rand == 7):
                text += "right"
                self.robot.move("right", self.env)
            print(text)

            time.sleep(1)

    def getRobot(self):
        return self.robot

    def setEnv(self, env):
        self.env = env
    

class envThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.env = epy.Environment(10)
        self.robot = None;

    def run(self):
        for i in range(15):
            self.env.gen()
            #On initialise de la poussière au démarage
        while(1):
            self.env.gen()
            time.sleep(1)
            self.env.display(self.robot.line, self.robot.row)
            #chaque seconde on génère ou pas aléatoirement soit de la poussière, soit un bijou, soit les deux sur une case, et on affiche l'état du manoir

    def getEnv(self):
        return self.env

    def setRobot(self, robot):
        self.robot = robot

athread = agentThread()
ethread = envThread()
athread.setEnv(ethread.getEnv())
ethread.setRobot(athread.getRobot())
ethread.start()
athread.start()
