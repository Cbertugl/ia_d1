#!/usr/bin/python

import threading
import time
import environment as epy
import agent as apy
import search as sc


class agentThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.robot = apy.Agent(0,0)
    def run(self):
        print("Agent running")
        #Algorithme de l'agent

class envThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.env = epy.Environment(10)

    def run(self):
        for i in range(15):
            self.env.gen()
            #On initialise de la poussière au démarage
        while(1):
            self.env.gen()
            time.sleep(1)
            self.env.display()
            #chaque seconde on génère ou pas aléatoirement soit de la poussière, soit un bijou, soit les deux sur une case, et on affiche l'état du manoir

athread = agentThread()
ethread = envThread()
athread.start()
ethread.start()
