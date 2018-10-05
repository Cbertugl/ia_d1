from abc import ABC, abstractmethod
import constants

class Agent:
    def __init__(self, line, row):
        # Position and energy init
        self.__line = line
        self.__row = row
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
    Vacuum the given room
    TODO: remove room parameter and make sure that the agent always have the room he is in in one attribute
    '''
    def vacuum(self, room):
        self.__vacuumEffector.act(room.getValue())
        self.__consumedEnergy += 1
        room.clean()
    
    '''
    Grab the jewel in the given room
    '''
    def grabJewel(self, room):
        self.__jewelGrabberEffector.act(room.getValue())
        self.__consumedEnergy += 1
        room.removeJewel()        
        
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
            print("Invalid moving order")
        
        self.__consumedEnergy += self.__consumedEnergy
        
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
