# Alarm Clock Class and Methods

class AlarmClock:

    def __init__(self):
        self.time = []
        self.alarm =  []
        self.a_time = ""

    def set_time(self):
        self.time = int(input("What time is it?\n"))
        print("The time is :", self.time)

    def set_alarm(self):
        self.alarm = int(input("What time do you want set the alarm for?\n"))
        print("Your alarm is set for", self.alarm)
    
    def alarm_set(self):
        self.a_time = input("Do you want to set your alarm? Y / N\n")
        if self.a_time == "Y":
            print("Alarm is set")
        elif self.a_time == "N":
            print("Alarm is not set")
