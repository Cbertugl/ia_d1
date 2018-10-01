#!/usr/bin/python

import threading
import time
import environment as epy
import agent as apy


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
        self.env = epy.Environment()

    def run(self):
        while(1):
            self.env.gen()
            time.sleep(1)
            self.env.display()

athread = agentThread()
ethread = envThread()
athread.start()
ethread.start()
