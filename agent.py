from abc import ABC, abstractmethod
import constants

class Agent:
    def __init__(self, line, row):
        # Position and energy init
        self.__line = line # Line number between 1 and the environment size
        self.__row = row # Row number between 1 and the environment size
        self.__room = None
        self.__consumedEnergy = 0

        # Sensors init
        self.__dustSensor = DustSensor()
        self.__jewelSensor = JewelSensor()

        # Effectors init
        self.__vacuumEffector = VacuumEffector()
        self.__jewelGrabberEffector = JewelGrabberEffector()

    def getPosition(self):
        return (self.__line, self.__row)

    def getEnergyConsumption(self):
        return self.__consumedEnergy

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
        if direction == "up" and self.__line > 1:
            self.__line -= 1
            
        elif direction == "down" and self.__line < e.height:
            self.__line += 1
        
        elif direction == "left" and self.__row > 1:
            self.__row -= 1
        
        elif direction == "right" and self.__row < e.width:
            self.__row += 1
            
        else:
            pass
        
        self.__consumedEnergy += self.__consumedEnergy
        self.__room = e.getRoom(self.__line, self.__row)
        
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
        print((elementValue == constants.JEWEL) or (elementValue == constants.DUST_AND_JEWEL))

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
