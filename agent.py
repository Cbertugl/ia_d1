from abc import ABC, abstractmethod
import constants
import environment
import search
import time

class Agent:
    # ==============================================================================================
    # CONSTRUCTOR
    # ==============================================================================================
    def __init__(self, size, room):
        # Position and energy init
        self.__state = "waiting..."
        self.__room = room
        self.__consumedEnergy = 0

        # Sensors init
        self.__dustSensor = DustSensor()
        self.__jewelSensor = JewelSensor()

        # Effectors init
        self.__vacuumEffector = VacuumEffector()
        self.__jewelGrabberEffector = JewelGrabberEffector()

        # BDI (beliefs, desires, intentions)
        self.__belief = None # No belief at the beginning
        self.__desire = environment.Environment(size) # Ideal environment is an empty one
        self.__intentions = [] # No intentions at the beginning

    # ==============================================================================================
    # GETTERS AND SETTERS
    # ==============================================================================================
    def getPosition(self):
        return self.__room.getPosition()

    def getEnergyConsumption(self):
        return self.__consumedEnergy

    def setBelief(self, belief):
        self.__belief = belief

    # ==============================================================================================
    # MAIN FUNCTIONS
    # ==============================================================================================
    '''
    Returns true if alive, false otherwise
    '''
    def isAlive(self):
        return True

    '''
    Returns an instance of Environment
    '''
    def observeEnvironmentWithMySensor(self, env):
        self.__state = "observing environment"

        size = env.getSize()
        belief = environment.Environment(size) # Empty environment
        map = env.getMap()

        for i in range(size):
            for j in range(size):
                room = map[i][j]
                roomValue = room.getValue()
                sensorValue = constants.NOTHING

                # Sensing room
                if(self.__dustSensor.detect(roomValue) and self.__jewelSensor.detect(roomValue)):
                    sensorValue = constants.DUST_AND_JEWEL
                elif(self.__dustSensor.detect(roomValue)): sensorValue = constants.DUST
                elif(self.__jewelSensor.detect(roomValue)): sensorValue = constants.JEWEL

                # Actualizing belief
                (roomLine, roomRow) = room.getPosition()
                belief.getRoom(roomLine, roomRow).setValue(sensorValue)

        return belief
    
    def chooseActions(self):
        self.__state = "choosing actions"
        # TODO: explore only if desire not reached ?
        #self.__intentions = search.mockSearch()
        #self.__intentions = search.breadthFirstSearch(self.__room)
        self.__intentions = search.aStarSearch(self.__room)
        
    def performActions(self, env):
        self.__state = "performing actions"

        action = None
        if(len(self.__intentions) > 0): action = self.__intentions.pop(0)

        while(action != None):
            if(action == constants.VACUUM): self.vacuum()
            elif(action == constants.GRAB_JEWEL): self.grabJewel()
            elif(action == constants.MOVE_UP): self.moveUp(env)
            elif(action == constants.MOVE_DOWN): self.moveDown(env)
            elif(action == constants.MOVE_LEFT): self.moveLeft(env)
            elif(action == constants.MOVE_RIGHT): self.moveRight(env)
            elif(action == constants.DO_NOTHING): self.doNothing()

            action = None
            if(len(self.__intentions) > 0): action = self.__intentions.pop(0)

    # ==============================================================================================
    # ACTIONS
    # ==============================================================================================
    '''
    Vacuum the actual room
    '''
    def vacuum(self):
        time.sleep(constants.AGENT_ACTION_TIME)
        self.__vacuumEffector.act(self.__room.getValue())
        self.__consumedEnergy += 1
        self.__room.clean()
    
    '''
    Grab the jewel in the actual room
    '''
    def grabJewel(self):
        time.sleep(constants.AGENT_ACTION_TIME)
        self.__jewelGrabberEffector.act(self.__room.getValue())
        self.__consumedEnergy += 1
        self.__room.removeJewel()
        
    def moveUp(self, env):
        time.sleep(constants.AGENT_ACTION_TIME)
        (line, row) = self.__room.getPosition()
        if line > 1:
            line -= 1
            self.__room = env.getRoom(line, row)
            self.__consumedEnergy += 1

    def moveDown(self, env):
        time.sleep(constants.AGENT_ACTION_TIME)
        (line, row) = self.__room.getPosition()
        if line < self.__belief.getSize():
            line += 1
            self.__room = env.getRoom(line, row)
            self.__consumedEnergy += 1

    def moveLeft(self, env):
        time.sleep(constants.AGENT_ACTION_TIME)
        (line, row) = self.__room.getPosition()
        if row > 1:
            row -= 1
            self.__room = env.getRoom(line, row)
            self.__consumedEnergy += 1

    def moveRight(self, env):
        time.sleep(constants.AGENT_ACTION_TIME)
        (line, row) = self.__room.getPosition()
        if row < self.__belief.getSize():
            row += 1
            self.__room = env.getRoom(line, row)
            self.__consumedEnergy += 1

    def doNothing(self):
        time.sleep(constants.AGENT_ACTION_TIME)

    # ==============================================================================================
    # DISPLAY
    # ==============================================================================================
    def display(self):
        # Belief
        (line, row) = self.getPosition()
        if(self.__belief != None): self.__belief.display(line, row)
        else: print("No belief yet")

        # State
        print("State: "+self.__state)

        # Intentions
        line = "Intentions: "
        for i in range(len(self.__intentions)):
            if(self.__intentions[i] == constants.VACUUM): line += "VACUUM"
            elif(self.__intentions[i] == constants.GRAB_JEWEL): line += "GRAB_JEWEL"
            elif(self.__intentions[i] == constants.MOVE_UP): line += "UP"
            elif(self.__intentions[i] == constants.MOVE_DOWN): line += "DOWN"
            elif(self.__intentions[i] == constants.MOVE_LEFT): line += "LEFT"
            elif(self.__intentions[i] == constants.MOVE_RIGHT): line += "RIGHT"
            elif(self.__intentions[i] == constants.DO_NOTHING): line += "DO_NOTHING"
            if(i != len(self.__intentions) - 1): line += ", "
        if(len(self.__intentions) == 0): line += "none"
        print(line)

        # Consumed energy
        print("Consumed energy:", self.__consumedEnergy)

        print("")

# ==================================================================================================
# SENSORS
# ==================================================================================================
class Sensor(ABC):
    def __init__(self):
        super().__init__()

    '''
    Returns true if it detects what it is build for, false otherwise
    '''
    @abstractmethod
    def detect(self, elementValue):
        pass

class DustSensor(Sensor):
    def detect(self, elementValue):
        return((elementValue == constants.DUST) or (elementValue == constants.DUST_AND_JEWEL))

class JewelSensor(Sensor):
    def detect(self, elementValue):
        return((elementValue == constants.JEWEL) or (elementValue == constants.DUST_AND_JEWEL))

# ==================================================================================================
# EFFECTORS
# ==================================================================================================
class Effector(ABC):
    def __init__(self):
        super().__init__()
    
    '''
    Returns nothing
    '''
    @abstractmethod
    def act(self):
        pass
    
class VacuumEffector(Effector):
    def __init__(self):
        self.nbDustVacuumed = 0 # number of dusts vacuumed
        self.nbJewelVacuumed = 0 # number of jewels vacuumed

        super().__init__()

    def act(self, elementValue):
        if(elementValue == constants.DUST): self.nbDustVacuumed += 1
        elif(elementValue == constants.JEWEL): self.nbJewelVacuumed += 1
        elif(elementValue == constants.DUST_AND_JEWEL):
            self.nbDustVacuumed += 1
            self.nbJewelVacuumed +=1

    def getNbDustVacuumed(self):
        return self.nbDustVacuumed

    def getNbJewelVacuumed(self):
        return self.nbJewelVacuumed

class JewelGrabberEffector(Effector):
    def __init__(self):
        self.nbJewelGrabbed = 0 # number of jewels grabbed

        super().__init__()

    def act(self, elementValue):
        if((elementValue == constants.JEWEL) or (elementValue == constants.DUST_AND_JEWEL)): self.nbJewelGrabbed += 1

    def getNbJewelGrabbed(self):
        return self.nbJewelGrabbed
