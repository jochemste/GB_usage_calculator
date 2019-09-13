from DateTime import DateTime
from GB_calculator import GB_calculator
from Cla_parser import Cla_parser

class Interface():
    def __init__(self):
        pass
    
    def __del__(self):
        pass

    def checkCLA(self):
        pass

    def displayHelp(self):
        print("Printing available Command Line Arguments:")
        print("<> Run program as loop, when no arguments are present")
        print("<i <nr_gb>> Show info once and exit (nr_gb = number of GB used)")
        print("<h> Show available Command Line Arguments")

    def displayInfo(self, data_usage):
        gbc = GB_calculator()
        dt = DateTime()
        days_remaining = dt.getMonthRange() - int(dt.getDate_dayOnly())
        print("Days in month: " + str(dt.getMonthRange()))
        print("Current day: " + dt.getDate_dayOnly())
        print("Days left: " + str(days_remaining))
        print("Max GB's: " + str(gbc.getMaxGB()))
        print("GB's left in total: " + str(gbc.getMaxGB() - data_usage))
        daily_average = "{0:.2f}".format(gbc.getDailyAverage(data_usage))
        future_average = "{0:.2f}".format(gbc.getFutureAverage(data_usage))
        print("Current daily average: " + daily_average + "GB")
        print("Future daily average: " + future_average + "GB")
        result = float(future_average) - float(daily_average)
        if result >= 0:
            print("Doing well! " + "{0:.2f}".format(result) + "GB's a day to spare")
        else:
            print("Slow it down, " + "{0:.2f}".format(result) + "GB's a day")

    def runAsLoop(self):
        user_input = ""        
        gbc = GB_calculator()
        dt = DateTime()
        data_usage = float(input("Used GB's: "))
        
        while user_input != "quit":        
            print("Select an option: ")
            user_input = input("<info> display all info, <set> Set contract max GB, <used> Set used GB's, <quit> end program\n")            
            
            if user_input == "info":
                self.displayInfo(data_usage)
            elif user_input == "set":
                gbc.setMaxGB(int(input("New Maximum GB's: ")))
                print("Max GB's updated")
                
            elif user_input == "used":
                data_usage = float(input("Used GB's: "))
                print("Used data updated")
                
            elif user_input == "quit":
                print("Exiting")
                break
            
            else:
                print("Invalid option")                
            print("\n")

    def runSingleTime(self):
        parser = Cla_parser()
        gbc = GB_calculator()
        dt = DateTime()
        indexDU = parser.getArgIndex("i")
        if indexDU > -1:
            indexDU = indexDU+1
            data_usage = float(parser.getArg(indexDU))
            if data_usage < 0:
                #exit
                pass
            self.displayInfo(data_usage)
            
    def startInterface(self):
        parser = Cla_parser()

        if parser.getArgc() == 1:
            self.runAsLoop()
        elif parser.argExists("i"):
            self.runSingleTime()
        elif parser.argExists("h"):
            self.displayHelp()
