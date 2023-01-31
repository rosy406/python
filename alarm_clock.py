#alarm.py

#define var


current_time = input("what is your current time?: ") 
    
alarm_time = input("in how many hours should the alarm go off in?: ")

current_time = int(current_time)

alarm_time = int(alarm_time)

#calculation

wakeup_time = (current_time + alarm_time) % 24

#print statement

print("The alarm will go off at", wakeup_time, "o,clock")