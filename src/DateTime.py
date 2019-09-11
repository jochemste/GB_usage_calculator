# -*- coding: utf-8 -*-
import datetime
from calendar import monthrange

class DateTime():
    printAll: bool
    def __init__(self, printAll: bool = False):
        self.printAll = printAll

    def __del__(self):
        pass

    def getDate(self):
        currentDate = datetime.datetime.now().strftime("%Y-%m-%d")
        if self.printAll == True:
            print("Current date: " + currentDate)            
        return currentDate

    def getDate_dayOnly(self):
        currentDate = datetime.datetime.now().strftime("%d")
        if self.printAll == True:
            print("Current date: " + currentDate)
        return currentDate

    def getDate_monthOnly(self):
        currentDate = datetime.datetime.now().strftime("%m")
        if self.printAll == True:
            print("Current date: " + currentDate)
        return currentDate

    def getDate_yearOnly(self):
        currentDate = datetime.datetime.now().strftime("%Y")
        if self.printAll == True:
            print("Current date: " + currentDate)
        return currentDate        

    def getTime(self):
        currentTime = datetime.datetime.now().strftime("%H:%M:%S")
        if self.printAll == True:
            print("Current time: " + currentTime)
        return currentTime

    def getMonthRange(self):
        month = int(self.getDate_monthOnly())
        year = int(self.getDate_yearOnly())
        range = monthrange(year, month)
        return range[1]
        

    ## @brief Returns true if a date is in the future, and false if it is not
    def date_in_future(self, date):
        currentDate= datetime.datetime.now()
        if date == currentDate.date() or date > currentDate.date():
            return True
        else:
            return False

    ## @brief Returns true if date1 is bigger and false if date2 is bigger or equal
    def compare_dates(self, date1, date2):
        return date1 < date2
