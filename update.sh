#!/bin/bash

set -e

if [ "$EUID" -ne 0 ]; then
  echo "Please run as root, e.g. 'sudo ./install.sh'!"
  exit
fi

if [ ! $(which python3) ]; then
  echo "Please install python3."
fi

if [ ! $(which systemctl) ]; then
  echo "Please install python3."
fi

systemctl stop fan-control.service
systemctl disable fan-control.service
systemctl daemon-reload

mkdir -p /opt/fan-control
cp fan-control.py /opt/fan-control/fan-control.py
cp fan-control.service /etc/systemd/system/fan-control.service

systemctl enable fan-control.service
systemctl start fan-control.service