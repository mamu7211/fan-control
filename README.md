# fan-control

Raspberry PI Fan Control.

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

