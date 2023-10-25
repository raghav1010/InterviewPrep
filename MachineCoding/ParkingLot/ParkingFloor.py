from ParkingSlotType import ParkingSlotType
from VehicleCategory import VehicleCategory
from Vehicle import Vehicle
from ParkingSlotType import ParkingSlotType
class ParkingFloor:

    def __init__(self,name,parkingSlots):
        self.name = name 
        self.parkingSlots = parkingSlots

    def getRelevantSlotForParking(self,vehicle):
        vehicleCategory = vehicle.getVehicleCategory()
        parkingSlotType = self.__pickCorrectSlot(vehicleCategory)
        relevantParkingSlots = self.parkingSlots.get(parkingSlotType)
        print(relevantParkingSlots)
        for m,val in relevantParkingSlots.items():
            print(m)
            print(val)
            if val.isAvailable==True:
                slot = val
                
                slot.addVehicle(vehicle)
                break 
        return slot 
    
    def __pickCorrectSlot(self,vehicleCategory):
        v = VehicleCategory()
        p = ParkingSlotType()
        if vehicleCategory == v.TwoWheeler:
            return p.TwoWheeler
        elif vehicleCategory == v.Hatchback or vehicleCategory == v.Sedan:
            return p.Compact 
        elif vehicleCategory == v.SUV:
            return p.Medium 
        elif vehicleCategory == v.Bus:
            return p.Large
        
        return None 


    