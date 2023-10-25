from datetime import datetime
from ParkingFloor import ParkingFloor
from Ticket import Ticket
class ParkingLot:

    def __init__(self,name):
        self.nameOfParkingLot = None 
        self.parkingFloors = None
        self.createParkingLot(name)
    
    def getNameOfParkingLot(self):
        return self.nameOfParkingLot
    
    def getParkingFloors(self):
        return self.parkingFloors
    
    def setNameOfParkingLot(self,name):
        self.nameOfParkingLot = name 
    
    def setParkingFloors(self,floors):
        self.parkingFloors = floors

    def createParkingLot(self,name):
        self.setNameOfParkingLot(name)
        self.setParkingFloors(list())

    def addFloors(self,floor):
        # floor = ParkingFloor(name,parkslots)
        self.parkingFloors.append(floor)
    
    def removeFloors(self, floor):
        self.parkingFloors.remove(floor)
    
    def assignTickets(self,vehicle):
        parkingSlot = self.__getParkingSlot(vehicle)
        if parkingSlot == None:
            return None 
        parkingTicket = self.__createTicketForSlot(parkingSlot,vehicle)
        return parkingTicket
    
    def scanAndPay(self,ticket):
        endTime = datetime.now()
        ticket.getParkingSlot().removeVehicle(ticket.getVehicle())
        duration = endTime - ticket.getStartTime()
        amount = duration.total_seconds() * ticket.getParkingSlot().getParkingSlotType()
        return amount

    def __getParkingSlot(self,vehicle):
        parkingSlot = None 
        for f in self.parkingFloors:
            parkingSlot = f.getRelevantSlotForParking(vehicle)
            if parkingSlot!=None:
                break 
        return parkingSlot
    
    def __createTicketForSlot(self,parkingSlot,vehicle):
        ticket = Ticket()
        return ticket.create(vehicle,parkingSlot)


    