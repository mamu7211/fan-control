# fan-control

fan-control is a simple fan controller script wrapped as systemd service. To run it you will need a 5V PWM fan that plugs into GND (Pin6), 5V (Pin4) and GIPO14 (Pin8), see [Raspberry Pi Documentation / GIPO and the 40-pin Header](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html).

## Prerequisits

1. If not already installed, install [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to clone this repo. Alternatively you can download this repository and execute all the steps that do not include git.
2. You need `python3`installed. Installation is done via `sudo apt install python3`.
3. You need to install module [gpiozero](https://gpiozero.readthedocs.io/en/latest/) in order to run. You can do this either by `sudo apt install python3-gpiozero` or `pip3 install gpiozero`.

## Installation

1. Go to your home directory `cd ~`.
2. Clone this repository `git clone https://github.com/mamu7211/fan-control.git`.
3. Cd into `cd fan-control`.
4. Install via `sudo ./install.sh`.

## Update

1. Cd into `cd ~/fan-control`.
2. Update the repository `git pull`.
2. Update the service via `sudo ./update.sh`.

## Removal

I have not created an uninstall script, just issue the following commands. Be careful when you issue the `rm` command. If in doubt read this [Introduction to systemd](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/chap-managing_services_with_systemd#sect-Managing_Services_with_systemd-Introduction).

```
sudo systemctl stop fan-control.service
sudo systemctl disable fan-control.service
sudo rm /etc/systemd/system/fan-control.service
sudo systemctl daemon-reload
``` 

## Check Installation

See the syslog if there is any output vial `tail -f /var/log/syslog`. fan-control logs the temperature each minute.

```
2023-11-15T15:53:13.258610+01:00 pi-k8s-04 systemd[1]: Reloading requested from client PID 313775 (unit session-3.scope)...
2023-11-15T15:53:13.258969+01:00 pi-k8s-04 systemd[1]: Reloading...
2023-11-15T15:53:17.736482+01:00 pi-k8s-04 systemd[1]: Reloading finished in 4473 ms.
2023-11-15T15:53:17.949732+01:00 pi-k8s-04 systemd[1]: Started fan-control.service - Raspberry PI Fan Control Service.
2023-11-15T15:53:18.235422+01:00 pi-k8s-01 fan-control.py: Turning on fan, temp is 43°c.
2023-11-15T15:53:18.236500+01:00 pi-k8s-04 fan-control.py: Current Temperature is 38°C.
```  