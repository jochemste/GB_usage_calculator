# main file for the GB usage calculator
from DateTime import DateTime
from GB_calculator import GB_calculator

def main():
    user_input = ""

    data_usage = -1

    gbc = GB_calculator()
    dt = DateTime()

    data_usage = float(input("Used GB's: "))

    while user_input != "quit":
        
        print("Select an option: ")
        user_input = input("<info> display all info, <set> Set contract max GB, <used> Set used GB's, <quit> end program\n")


        if user_input == "info":
            #data_usage = int(input("GB's used this month: "))
            days_remaining = dt.getMonthRange() - int(dt.getDate_dayOnly())
            print("Days in month: " + str(dt.getMonthRange()))
            print("Current day: " + dt.getDate_dayOnly())
            print("Days left: " + str(days_remaining))
            print("Max GB's: " + str(gbc.getMaxGB()))
            daily_average = "{0:.2f}".format(gbc.getDailyAverage(data_usage))
            future_average = "{0:.2f}".format(gbc.getFutureAverage(data_usage))
            print("Current daily average: " + daily_average + "GB")
            print("Future daily average: " + future_average + "GB")
            result = float(future_average) - float(daily_average)
            if result >= 0:
                print("Doing well! " + "{0:.2f}".format(result) + "GB's a day to spare")
            else:
                print("Slow it down, " + "{0:.2f}".format(result) + "GB's a day")
            
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

if __name__ == "__main__":
    main()
