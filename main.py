#!/usr/bin/python

import constants
import threading
import time
import environment as epy
import agent as apy
import random
import search as sc

# ==================================================================================================
# THREADS
# ==================================================================================================
class agentThread(threading.Thread):
    def __init__(self, agent, env):
        threading.Thread.__init__(self)
        self.__robot = agent
        self.__env = env

    def run(self):
        print("Aspirobot T-0.1 running")

        while(1):
            # TODO: algorithme de l'agent
            rand = random.randint(0,9)
            if(rand == 0 or rand == 1):
                self.__robot.move("up", self.__env)
            if(rand == 2 or rand == 3):
                self.__robot.move("down", self.__env)
            if(rand == 4 or rand == 5):
                self.__robot.move("left", self.__env)
            if(rand == 6 or rand == 7):
                self.__robot.move("right", self.__env)

            self.__robot.vacuum()

            time.sleep(constants.AGENT_ACTION_TIME)

class envThread(threading.Thread):
    def __init__(self, env, agent):
        threading.Thread.__init__(self)
        self.__env = env
        self.__robot = agent

    def run(self):
        print("Environment running")

        while(1):
            #chaque seconde on génère ou pas aléatoirement soit de la poussière, soit un bijou, soit les deux sur une case, et on affiche l'état du manoir
            self.__env.gen()

            (robotLine, robotRow) = self.__robot.getPosition()
            self.__env.display(robotLine, robotRow)
            
            time.sleep(1)

# ==================================================================================================
# MAIN
# ==================================================================================================
# Creating environment and agent
envSize = 10
(line, row) = (random.randint(1, envSize), random.randint(1, envSize)) # Initial robot position

env = epy.Environment(envSize)
agent = apy.Agent(line, row)

env.initElements() # We create some initial dust and jewels

# Creating threads
athread = agentThread(agent, env)
ethread = envThread(env, agent)

# Starting threads
ethread.start()
athread.start()
