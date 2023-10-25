class Vehicle:
    def __init__(self,vehicleNumber,vehicleCategory):
        self.vehicleNumber = None 
        self.vehicleCategory = None
        self.setVehicleNumber(vehicleNumber)
        self.setVehicleCategory(vehicleCategory)
    
    def setVehicleNumber(self,vehicleNumber):
        self.vehicleNumber = vehicleNumber
    
    def setVehicleCategory(self,vehicleCategory):
        self.vehicleCategory = vehicleCategory
    
    def getVehicleNumber(self):
        return self.vehicleNumber
    
    def getVehicleCategory(self):
        return self.vehicleCategory
    