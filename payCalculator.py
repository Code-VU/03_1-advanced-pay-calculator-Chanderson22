def calculatePay():
    # This first line is provided for you
    hrs = input("Enter Hours: ")
    try:
        hours = float(hrs)
    except: 
        print("Error, please enter numeric input")
        exit()
    rte = input("Enter Rate: ")
    try:
        rate = float(rte)
    except: 
        print("Error, please enter numeric input")
        exit()
    pay = hours*rate
    if hours > 40:
        OT_pay = (hours-40.0)*(rate*0.5)
        pay = pay+OT_pay
        print ("Pay:", pay)
    else:
        print ("Pay:", pay)
    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
