import time
from ParkingFloor import ParkingFloor
from ParkingLot import ParkingLot
from ParkingSlot import ParkingSlot
from ParkingSlotType import ParkingSlotType
from VehicleCategory import VehicleCategory
from Vehicle import Vehicle
class ParkingMain:

    def start(self):
        p = ParkingSlotType()
        nameOfParkingLot = "Pintoss Parking Lot"
        allSlots = dict()
   
    
        compactSlot = dict()
        compactSlot["C1"]=ParkingSlot("C1",p.Compact)
        compactSlot["C2"]=ParkingSlot("C2",p.Compact)
        compactSlot["C3"]=ParkingSlot("C3",p.Compact)
        allSlots[p.Compact] = compactSlot

        largeSlot = dict()
        largeSlot["L1"]=ParkingSlot("L1",p.Large)
        largeSlot["L2"]=ParkingSlot("L2",p.Large)
        largeSlot["L3"]=ParkingSlot("L3",p.Large)
        allSlots[p.Large] = largeSlot


        parkingFloor = ParkingFloor("1",allSlots)
        parkingLot = ParkingLot(nameOfParkingLot)
        parkingLot.addFloors(parkingFloor)

        vehicle = Vehicle(None,None)
        vehicle.setVehicleNumber("KA100")
        vehicle.setVehicleCategory(VehicleCategory.Hatchback)

        ticket = parkingLot.assignTickets(vehicle)
        print("Ticket Number :",ticket.getTicketNumber())

        time.sleep(10)

        print(parkingLot.scanAndPay(ticket))
        print("______________________________________________________________________________")
        vehicle = Vehicle(None,None)
        vehicle.setVehicleNumber("RBS200")
        vehicle.setVehicleCategory(VehicleCategory.Bus)

        ticket = parkingLot.assignTickets(vehicle)
        print("Ticket Number :",ticket.getTicketNumber())

        time.sleep(5)
        
        print(parkingLot.scanAndPay(ticket))

obj = ParkingMain()
obj.start()