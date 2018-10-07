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
        
        evaluation_rate = 3                 # Performance will be evaluated every n + 1 cycle
        evaluation_loop = evaluation_rate   # Variable to keep track of the performance evaluation loop
        
        while(self.__robot.isAlive()):
            # Observing environment
            observation = self.__robot.observeEnvironmentWithMySensor(self.__env)

            # Updating belief
            self.__robot.setBelief(observation)

            # Exploring
            self.__robot.chooseActions()

            # Performing intentions
            self.__robot.performActions(self.__env)
            
            # Evaluating performance
            if evaluation_loop == 0 : 
                self.__robot.evaluatePerformance()
                evaluation_loop = evaluation_rate
            else : evaluation_loop = evaluation_loop - 1
            
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

            time.sleep(constants.ENVIRONMENT_GENERATION_TIME)

class displayThread(threading.Thread):
    def __init__(self, env, agent):
        threading.Thread.__init__(self)
        self.__env = env
        self.__agent = agent

    def run(self):
        while(1):
            print("=== ENVIRONNEMENT ===")
            self.__env.display()

            print("======= ROBOT =======")
            self.__agent.display()

            time.sleep(1)

# ==================================================================================================
# MAIN
# ==================================================================================================
# Creating environment and agent
envSize = 10
(line, row) = (random.randint(1, envSize), random.randint(1, envSize)) # Initial robot position

env = epy.Environment(envSize)
agent = apy.Agent(envSize, env.getRoom(line, row))

env.initElements() # We create some initial dust and jewels

# Creating threads
athread = agentThread(agent, env)
ethread = envThread(env, agent)
dthread = displayThread(env, agent)

# Starting threads
ethread.start()
athread.start()
dthread.start()
