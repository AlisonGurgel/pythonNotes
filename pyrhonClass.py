class Car:
    def __init__(this, n, y):
        this.carName = n
        this.carYear = y
        this.attFunc = print(this.carName, "\_/", this.carYear)
        
    def getYear(this):
        print(this.carYear)

    def start(that, km):
        print(f"{that.carName} start moving at {km}kmh")

c1 = Car("BMW", 1990)

c1.start(10)
c1.getYear()
c1.attFunc
