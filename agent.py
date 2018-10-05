from abc import ABC, abstractmethod
import constants

class Agent:
    
    def __init__(self, line, row):
        # Position and energy init
        self.line = line
        self.row = row
        self.consumedEnergy = 0

        # Sensors init
        self.dustSensor = DustSensor()
        self.jewelSensor = JewelSensor()

        # Effectors init
        self.vacuumEffector = VacuumEffector()
        self.jewelGrabberEffector = JewelGrabberEffector()

    def getEnergyConsumption(self):
        return self.consumedEnergy

    '''
    Vacuum the given room
    '''
    def vacuum(self, room):
        self.vacuumEffector.act(room.getValue())
        self.consumedEnergy += 1
        room.clean()
    
    '''
    Grab the jewel in the given room
    '''
    def grabJewel(self, room):
        self.jewelGrabberEffector.act(room.getValue())
        self.consumedEnergy += 1
        room.removeJewel()        
        
    def move(self, direction, e):
        if direction == "up" and self.line > 1:
            self.line -= 1
            
        elif direction == "down" and self.line < e.height:
            self.line += 1
        
        elif direction == "left" and self.row > 1:
            self.row -= 1
        
        elif direction == "right" and self.row < e.width:
            self.row += 1
            
        else:
            print("Invalid moving order")
        
        self.consumedEnergy += self.consumedEnergy
        
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
