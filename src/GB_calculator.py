from DateTime import DateTime

class GB_calculator():
    printAll: bool
    file: str
    dt: DateTime
    
    def __init__(self, printAll: bool= False):
        self.printAll = printAll
        self.file = "max_gb.txt"
        self.dt= DateTime()

    def setMaxGB(self, max_gb):
        with open(self.file, 'w') as data_file:
            data_file.truncate(0)
            data_file.write(str(max_gb))

    def getMaxGB(self):
        with open(self.file, 'r') as data_file:
            max_gb = int(data_file.read())
            return max_gb

    def getDailyAverage(self, data_used: int):
        days_passed = int(self.dt.getDate_dayOnly())
        return data_used / days_passed

    def getFutureAverage(self, data_used: int):
        days_passed = int(self.dt.getDate_dayOnly())
        month_range = self.dt.getMonthRange()
        return (self.getMaxGB() - data_used) / (month_range - days_passed)
        
