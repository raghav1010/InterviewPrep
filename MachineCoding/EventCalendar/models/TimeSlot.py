class TimeSlot(object):

    _startTime = None 
    _endTime = None 

    def __init__(self,startTime,endTime): 
        self._startTime = startTime 
        self._endTime = endTime 
    
    def getStartTime(self):
        return self._startTime 
    
    def getEndTime(self):
        return self._endTime 
    

    
    