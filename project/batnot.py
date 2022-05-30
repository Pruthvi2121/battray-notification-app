from operator import contains
import psutil
from notifypy import Notify
notification=Notify()
import os

os.chdir("C:\project")
while True:
    battery=psutil.sensors_battery()
    pulg=battery.power_plugged
    percent=battery.percent
    

    if pulg:
        
        if percent>60:
            notification.title="Battery is above 90 % plug off the charger"
            notification.message="To avoid overcharging , Make sure to plug off the charger\nIt will save your battery life "
            notification.send()
            continue
        
        

    