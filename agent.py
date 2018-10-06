from abc import ABC, abstractmethod
import constants
import environment

class Agent:
    def __init__(self, room):
        # Position and energy init
        self.__room = room
        self.__consumedEnergy = 0

        # Sensors init
        self.__dustSensor = DustSensor()
        self.__jewelSensor = JewelSensor()

        # Effectors init
        self.__vacuumEffector = VacuumEffector()
        self.__jewelGrabberEffector = JewelGrabberEffector()

        # BDI (beliefs, desires, intentions) TODO: finish
        self.__belief = None
        # self.__desire = environment.Environment()
        #self.__intentions = 

    def getPosition(self):
        return self.__room.getPosition()

    def getEnergyConsumption(self):
        return self.__consumedEnergy

    def setBelief(self, belief):
        self.__belief = belief

    '''
    Returns true if alive, false otherwise
    '''
    def isAlive(self):
        # We could use the belief here to determine whether we are alive or not
        return True

    '''
    Returns an instance of Environment
    '''
    def observeEnvironmentWithMySensor(self, env):
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

    '''
    Vacuum the actual room
    '''
    def vacuum(self):
        self.__vacuumEffector.act(self.__room.getValue())
        self.__consumedEnergy += 1
        self.__room.clean()
    
    '''
    Grab the jewel in the actual room
    '''
    def grabJewel(self):
        self.__jewelGrabberEffector.act(self.__room.getValue())
        self.__consumedEnergy += 1
        self.__room.removeJewel()        
        
    def move(self, direction, e):
        (line, row) = self.__room.getPosition()
        if direction == "up" and line > 1:
            line -= 1
            
        elif direction == "down" and line < e.getSize():
            line += 1
        
        elif direction == "left" and row > 1:
            row -= 1
        
        elif direction == "right" and row < e.getSize():
            row += 1
            
        else:
            pass
        
        self.__consumedEnergy += self.__consumedEnergy
        self.__room = e.getRoom(line, row)
        
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
        self.nbDustVacuumed = 0 # number of dust vacuumed
        self.nbJewelVacuumed = 0 # number of jewel vacuumed

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
        self.nbJewelGrabbed = 0 # number of dust grabbed

        super().__init__()

    def act(self, elementValue):
        if((elementValue == constants.JEWEL) or (elementValue == constants.DUST_AND_JEWEL)): self.nbJewelGrabbed += 1

    def getNbJewelGrabbed(self):
        return self.nbJewelGrabbed
