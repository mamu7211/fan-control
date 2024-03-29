from gpiozero import PWMLED, CPUTemperature
from time import sleep
import syslog

fan = PWMLED(14)

limits = {
    "limit_1" : {
        "on" : 40,
        "off" : 35,
    }
}

counter = 0

while True:
    cpuTemp = round(CPUTemperature().temperature)
    if fan.value < 1.0 and cpuTemp >= 50:
        syslog.syslog(syslog.LOG_INFO, f"Turning on fan, temp is {cpuTemp}°c.")
        fan.value = 1.0
    elif fan.value > 0.0 and cpuTemp <= 45:
        syslog.syslog(syslog.LOG_INFO, f"Turning off fan, temp is {cpuTemp}°c.")
        fan.value = 0.0
    if counter % 6 == 0:
        syslog.syslog(syslog.LOG_INFO, f"Current Temperature is {cpuTemp}°C.")
    sleep(10)
    counter += 1