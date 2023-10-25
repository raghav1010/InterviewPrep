class ParkingSlot:

    def __init__(self,name,parkingSlotType):
        self.name = name 
        self.isAvailable = True 
        self.vehicle = None 
        self.parkingSlotType = parkingSlotType 
    
    def addVehicle(self,vehicle):
        self.vehicle = vehicle
        self.isAvailable = False 
    
    def removeVehicle(self,vehicle):
        self.vehicle = None 
        self.isAvailable = True 

    def getParkingSlotType(self):
        return self.parkingSlotType
