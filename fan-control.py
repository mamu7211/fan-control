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

try:
    while True:
        cpu = round(CPUTemperature().temperature)
        print(f"temp={cpu}°C, fan={round(fan.value*100)}%")
        if fan.value < 0.3 and cpu >= 40:
            fan.value = 0.3
        if fan.value < 1.0 and cpu >= 60:
            fan.value = 1.0
        elif fan.value > 0.0 and cpu <= 35:
            fan.value = 0.0
        counter += 1
        syslog.syslog(syslog.LOG_INFO, f"TEMP {counter}")
        sleep(5)
except:
    syslog.syslog(syslog.LOG_ALERT, 'Resetting fan speed...')
    fan.value = 1
