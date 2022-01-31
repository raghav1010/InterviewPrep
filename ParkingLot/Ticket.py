from datetime import datetime
class Ticket:

    def __init__(self):
        self.ticketNumber = None
        self.startTime = None
        self.endTime = None
        self.vehicle = None
        self.parkingSlot = None 
    
    def create(self,vehicle,parkingSlot):
        now = datetime.now()
        snow = now.strftime("%H:%M:%S")
        self.ticketNumber = str(vehicle.getVehicleNumber())+snow 
        self.startTime = now 
        self.endTime = None 
        self.vehicle = vehicle
        self.parkingSlot = parkingSlot
        return self

    def getTicketNumber(self):
        return self.ticketNumber
    
    def getStartTime(self):
        return self.startTime
    
    def getEndTime(self):
        return self.endTime
    
    def getVehicle(self):
        return self.vehicle
    
    def getParkingSlot(self):
        return self.parkingSlot
        